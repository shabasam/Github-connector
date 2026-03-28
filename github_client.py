import httpx
from fastapi import HTTPException
from config import settings

class GitHubClient:
    def __init__(self):
        self.base_url = settings.GITHUB_API_URL
        if not settings.GITHUB_PAT:
            print("WARNING: GITHUB_PAT is not set. API calls requiring authentication will fail.")
        
        self.headers = {
            "Accept": "application/vnd.github.v3+json",
            "Authorization": f"Bearer {settings.GITHUB_PAT}" if settings.GITHUB_PAT else ""
        }

    async def _request(self, method: str, endpoint: str, **kwargs):
        async with httpx.AsyncClient() as client:
            url = f"{self.base_url}{endpoint}"
            try:
                response = await client.request(method, url, headers=self.headers, **kwargs)
                response.raise_for_status()
                return response.json()
            except httpx.HTTPStatusError as e:
                # GitHub specific error handling can be done here.
                raise HTTPException(status_code=e.response.status_code, detail=f"GitHub API Error: {e.response.text}")
            except httpx.RequestError as e:
                raise HTTPException(status_code=500, detail=f"Failed to connect to GitHub API: {str(e)}")

    async def get_user_repositories(self, username: str):
        return await self._request("GET", f"/users/{username}/repos")

    async def list_repository_issues(self, owner: str, repo: str):
        return await self._request("GET", f"/repos/{owner}/{repo}/issues")

    async def create_issue(self, owner: str, repo: str, title: str, body: str = None):
        if not settings.GITHUB_PAT:
             raise HTTPException(status_code=401, detail="Authentication required to create issues. Please set GITHUB_PAT.")
             
        payload = {"title": title}
        if body:
            payload["body"] = body
            
        return await self._request("POST", f"/repos/{owner}/{repo}/issues", json=payload)
