import secrets
from dotenv import load_dotenv
import os
from pydantic import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    API_V1_STR: str = os.getenv('API_V1_STR')
    PROJECT_NAME: str = os.getenv('PROJECT_NAME')
    SECRET_KEY: str = secrets.token_urlsafe(32)

    class Config:
        env_file = ".env"


settings = Settings()
