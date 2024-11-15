from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    ig_client_id: str
    ig_client_secret: str
    ig_grant_type: str = "authorization_code"
    ig_redirect_uri: str

    class Config:
        env_file = ".env"