from pydantic import BaseModel
from src.settings import Settings

settings = Settings()

class AccessTokenDTO(BaseModel):
    client_id: str = settings.ig_client_id
    client_secret: str = settings.ig_client_secret
    grant_type: str = settings.ig_grant_type
    redirect_uri: str = settings.ig_redirect_uri
    code: str

class CodeDTO(BaseModel):
    code: str

class ReplyDTO(BaseModel):
    comment_id: str
    message: str
    access_token: str