from fastapi import FastAPI
from router import blog_get, blog_post


app = FastAPI()
app.include_router(blog_get.router)
app.include_router(blog_post.router)


@app.get(
    "/",
    tags=["Home"],
    summary="Blog home page",
    description="Hello World! Very First API",
    response_description='Successful Response',
)
def home():
    return "Hello World! Very First API"
