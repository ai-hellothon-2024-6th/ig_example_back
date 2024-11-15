import requests
from requests.exceptions import HTTPError

def get_access_token(data: dict) -> dict:
    url = "https://api.instagram.com/oauth/access_token"
    response = requests.post(url, data=data)
    response.raise_for_status()
    return response.json()

def get_me(access_token: str) -> dict:
    url = "https://graph.instagram.com/me"
    params = {
        "fields": ",".join(["user_id", "username", "name", "profile_picture_url",
                            "followers_count", "follows_count", "media_count"]),
        "access_token": access_token
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

def get_media_id_list(user_id: str, access_token: str) -> dict:
    url = f"https://graph.instagram.com/{user_id}/media"
    params = {
        "access_token": access_token
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

def get_media_one(media_id: str, access_token: str) -> dict:
    url = f"https://graph.instagram.com/{media_id}"
    params = {
        "fields": ",".join(["id", "media_type", "media_url",
                            "thumbnail_url", "permalink", "caption",
                            "timestamp", "comments_count", "like_count"]),
        "access_token": access_token
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

def get_comments(media_id: str, access_token: str) -> dict:
    url = f"https://graph.instagram.com/{media_id}/comments"
    params = {
        "access_token": access_token,
        "fields": ",".join(["id", "text", "timestamp", "username"])
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

def reply_comment(comment_id: str, comment: str, access_token: str) -> dict:
    url = f"https://graph.instagram.com/{comment_id}/replies"
    data = {
        "access_token": access_token,
        "text": comment
    }
    response = requests.post(url, data=data)
    response.raise_for_status()
    return response.json()