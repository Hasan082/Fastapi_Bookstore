from fastapi import APIRouter, status, Response
from enum import Enum
from typing import Optional

router = APIRouter(
    prefix="/blog",
    tags=["Blog"],
)


@router.get("/all")
def get_all_blogs(page=1, page_size=10):
    return {"message": f"This is {page} blogs and page size is {page_size}"}


@router.get("/{id}/comments/{comment_id}", tags=["Comment"])
def get_comment(id: int, comment_id: int, valid: bool = True, username:
                Optional[str] = None):
    """
        Start Retriving commnets
        - **id**: blog id & mandatory parameter
        - **comment_id**: comment id & mandatory parameter
        - **valid**: optional query parameter
        - **username**: optional query parameter
    """
    return {"message": f"this is comment {comment_id} of blog {id} it's {valid} and username is {username}"}


class BlogType(str, Enum):
    story = 'story'
    howto = 'howto'
    news = 'news'


@router.get("/{type}")
def get_blog_type(type: BlogType):
    return {"message": f"{type} blogs"}


@router.get("/{id}")
def get_blog(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': 'blog not found'}
    else:
        response.status_code = status.HTTP_200_OK
        return {"message": f"this is blog {id}"}
