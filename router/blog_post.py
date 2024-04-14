from fastapi import APIRouter, status


router = APIRouter(
    prefix="/blog",
    tags=["Blog"],
)


@router.post("/new-post", status_code=status.HTTP_201_CREATED)
def create_blog():
    return {"message": "Blog created"}
