from fastapi import FastAPI, Request, Response
from pydantic import BaseModel

app = FastAPI()

BOOKS = [
    {'title': 'title 1', 'author': 'Author 1', 'category': 'Math'},
    {'title': 'title 2', 'author': 'Author 2', 'category': 'Science'},
    {'title': 'title 3', 'author': 'Author 3', 'category': 'Science'},
    {'title': 'title 4', 'author': 'Author 4', 'category': 'History'},
    {'title': 'title 5', 'author': 'Author 5', 'category': 'Science'},
    {'title': 'title 6', 'author': 'Author 6', 'category': 'History'},
]


class Book(BaseModel):
    title: str
    author: str
    category: str


@app.get("/books")
def books():
    return BOOKS


@app.get("/books/{book_title}")
def read_books(book_title: str):
    for book in BOOKS:
        if book.get('title') == book_title:
            return book


@app.get("/books/")
def books_category_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


@app.get("/books/{book_author}/")
def books_act_and_author(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and \
                book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


@app.post("/books/create_book")
def create_books(book_title: str, author: str, category: str):
    new_Book = {"title": book_title, "author": author, "category": category}
    BOOKS.append(new_Book)


@app.put("/books/update_book/")
def update_book(book: Book):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == book.title.casefold():
            BOOKS[i] = book.dict()
            return {"message": "Book updated successfully", "book": BOOKS[i]}
