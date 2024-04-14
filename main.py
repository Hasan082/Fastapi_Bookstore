from fastapi import FastAPI, status, Response
from enum import Enum
from typing import Optional

app = FastAPI()


@app.get(
        "/",
        tags=["Home"],
        summary="Blog home page",
        description="Hello World! Very First API",
        response_description='Successful Response',
    )
def home():
    return "Hello World! Very First API"


@app.get("/blog/all", tags=["Blog"])
def get_all_blogs(page=1, page_size=10):
    return {"message": f"This is {page} blogs and page size is {page_size}"}


@app.get("/blog/{id}/comments/{comment_id}", tags=["Comment"])
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


@app.get("/blog/{type}", tags=["Blog"])
def get_blog_type(type: BlogType):
    return {"message": f"{type} blogs"}


@app.get("/blog/{id}", tags=["Blog"])
def get_blog(id: int, response: Response):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': 'blog not found'}
    else:
        response.status_code = status.HTTP_200_OK
        return {"message": f"this is blog {id}"}

