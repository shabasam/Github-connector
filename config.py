from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    GITHUB_PAT: str = "GITHUB_PAT"
    GITHUB_API_URL: str = "https://api.github.com"
    
    class Config:
        env_file = ".env"

settings = Settings()
