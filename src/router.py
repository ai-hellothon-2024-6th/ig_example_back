from fastapi import APIRouter, Response

from src.models import *
from src.api import *

router = APIRouter()

@router.post("/access_token")
def code_to_access_token(dto: CodeDTO):
    access_token_dto = AccessTokenDTO(code=dto.code)
    try:
        result = get_access_token(access_token_dto.model_dump())
    except HTTPError as e:
        return Response(
            content=e.response.text,
            status_code=e.response.status_code
        )
    return {
        "access_token": result["access_token"]
    }

# TODO : long-live access token
# TODO : redis
# TODO : jwt

@router.get("/me")
def me(access_token: str):
    try:
        result = get_me(access_token)
    except HTTPError as e:
        return Response(
            content=e.response.text,
            status_code=e.response.status_code
        )
    return result

@router.get("/media")
def media(user_id: str, access_token: str):
    try:
        media_id_list = get_media_id_list(user_id, access_token)['data']
        result = [get_media_one(media['id'], access_token) for media in media_id_list]
        for m in result:
            m['comments'] = get_comments(m['id'], access_token)["data"]
    except HTTPError as e:
        return Response(
            content=e.response.text,
            status_code=e.response.status_code
        )
    return result

@router.post("/reply")
def reply(dto: ReplyDTO):
    try:
        print(1)
        result = reply_comment(dto.comment_id, dto.message, dto.access_token)
        print(2)
    except HTTPError as e:
        return Response(
            content=e.response.text,
            status_code=e.response.status_code
        )
    return result