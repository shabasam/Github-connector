# GitHub Cloud Connector

A REST API backend connected to GitHub's API, built with **FastAPI**. It allows you to:
- List public repositories for a user.
- List issues for a given repository.
- Create an issue in a repository.

## Requirements
- Python 3.8+
- Personal Access Token (PAT) from GitHub (for creating issues).

## Tech Stack
- Python
- FastAPI
- Uvicorn
- HTTPX
- Pydantic

## Project Structure
- `main.py` - FastAPI application entry point, containing API routes.
- `github_client.py` - Handles direct HTTP communication with GitHub API and error handling.
- `schemas.py` - Pydantic models for request/response validation.
- `config.py` - Loads environment variables securely.

## Setup Instructions

1. Clone or copy the source code to a local directory.
2. Navigate into the directory:
   ```bash
   cd github-connector
   ```
3. Create a Python virtual environment:
   ```bash
   python -m venv venv
   ```
4. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On Mac/Linux: `source venv/bin/activate`
5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
6. Setup Authentication (Required for creating issues):
   - Get a GitHub PAT (Personal Access Token) with `repo` scope or specific repository Issues permissions (Read/Write).
   - Create a `.env` file in the root directory:
     ```env
     GITHUB_PAT=your_github_personal_access_token_here
     ```

## How to Run the Project
Start the development server:
```bash
uvicorn main:app --reload
```
The application will be available at `http://localhost:8000`.

## API Endpoints & Usage

FastAPI automatically generates an interactive Swagger UI. Open your browser and navigate to:
**http://localhost:8000/docs**

### Available Endpoints
- `GET /` - API Health check / Welcome message.
- `GET /repos/{username}` - Returns a list of repositories for a specified user.
- `GET /repos/{owner}/{repo}/issues` - Lists issues for a repository.
- `POST /repos/{owner}/{repo}/issues` - Creates an issue. Requires `GITHUB_PAT` configured.
  ```json
  {
    "title": "Bug found",
    "body": "Detailed description..."
  }
  ```

### Example Usage Using cURL

Fetch user repos:
```bash
curl -X GET http://localhost:8000/repos/octocat
```

Create an issue:
```bash
curl -X POST http://localhost:8000/repos/octocat/hello-world/issues \
     -H "Content-Type: application/json" \
     -d '{"title": "Testing Connector", "body": "This is a test issue."}'
```
