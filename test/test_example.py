from fastapi.testclient import TestClient
from books import app

client = TestClient(app)


# Test cases for GET endpoints
def test_get_all_books():
    response = client.get("/books")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_book_by_title():
    response = client.get("/books/title 1")
    assert response.status_code == 200
    assert response.json() == {'title': 'title 1', 'author': 'Author 1', 'category': 'Math'}


def test_get_books_by_category():
    response = client.get("/books/?category=Science")
    assert response.status_code == 200
    books = response.json()
    assert all(book['category'] == 'Science' for book in books)


def test_get_books_by_author_and_category():
    response = client.get("/books/Author 2/?category=Science")
    assert response.status_code == 200
    books = response.json()
    assert all(book['author'] == 'Author 2' and book['category'] == 'Science' for book in books)


def test_create_book():
    new_book = {
        "book_title": "title 7",
        "author": "Author 7",
        "category": "Philosophy"
    }
    response = client.post("/books/create_book", json=new_book)

    # Assert that the response status code is 422 (Unprocessable Entity)
    assert response.status_code == 422


# Test cases for PUT endpoint


def test_update_book():
    updated_book = {
        "title": "title 1",
        "author": "Updated Author",
        "category": "Updated Category"
    }
    response = client.put("/books/update_book/", json=updated_book)
    assert response.status_code == 200
    assert response.json() == {"message": "Book updated successfully", "book": updated_book}


# Test cases for DELETE endpoint
def test_delete_existing_book():
    response_delete = client.delete("/books/delete_book/title 1")
    assert response_delete.status_code == 200
    assert response_delete.json() == {"message": "Book deleted successfully", "book": "title 1"}


def test_delete_non_existing_book():
    response_delete = client.delete("/books/delete_book/non_existing_title")
    assert response_delete.status_code == 404
    assert response_delete.json() == {"detail": "Book not found"}
