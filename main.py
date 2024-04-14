from fastapi import FastAPI
from router import blog_get


app = FastAPI()
app.include_router(blog_get.router)


@app.get(
    "/",
    tags=["Home"],
    summary="Blog home page",
    description="Hello World! Very First API",
    response_description='Successful Response',
)
def home():
    return "Hello World! Very First API"
