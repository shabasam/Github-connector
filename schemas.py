from pydantic import BaseModel
from typing import Optional

class IssueCreate(BaseModel):
    title: str
    body: Optional[str] = None
    
class RepositoryResponse(BaseModel):
    id: int
    name: str
    full_name: str
    html_url: str
    description: Optional[str] = None

class IssueResponse(BaseModel):
    id: int
    number: int
    title: str
    state: str
    html_url: str
    body: Optional[str] = None
