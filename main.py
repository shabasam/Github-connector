from fastapi import FastAPI
from typing import List
from github_client import GitHubClient
import schemas

app = FastAPI(
    title="GitHub Cloud Connector",
    description="A simple API connector to GitHub for fetching repos, listing and creating issues.",
    version="1.0.0"
)

github_client = GitHubClient()

@app.get("/")
def read_root():
    return {"message": "Welcome to GitHub Cloud Connector API. Checkout /docs for endpoints."}

@app.get("/repos/{username}", response_model=List[schemas.RepositoryResponse], summary="List repositories for a user")
async def get_user_repos(username: str):
    """
    Fetches the public repositories for a specified GitHub user.
    If authenticated, it might fetch more details based on the token scope. \n
    **username**: The GitHub username (e.g., 'octocat').
    """
    return await github_client.get_user_repositories(username)

@app.get("/repos/{owner}/{repo}/issues", response_model=List[schemas.IssueResponse], summary="List issues for a repository")
async def list_issues(owner: str, repo: str):
    """
    Lists issues for a given repository. \n
    **owner**: Repository owner (e.g., username or organization). \n
    **repo**: Repository name.
    """
    return await github_client.list_repository_issues(owner, repo)

@app.post("/repos/{owner}/{repo}/issues", response_model=schemas.IssueResponse, summary="Create an issue in a repository")
async def create_issue(owner: str, repo: str, issue_data: schemas.IssueCreate):
    """
    Creates a new issue in the specified repository. \n
    Requires an authenticated Personal Access Token (PAT) with appropriate scopes (e.g., 'repo' scope). \n
    **owner**: Repository owner. \n
    **repo**: Repository name. \n
    **issue_data**: JSON payload containing 'title' and optional 'body'.
    """
    return await github_client.create_issue(owner, repo, issue_data.title, issue_data.body)
