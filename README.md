# FastAPI Bookstore API

A simple FastAPI application to manage a collection of books.

## Table of Contents

1. [Installation](#installation)
2. [Quick Start](#quick-start)
3. [Project Structure](#project-structure)
4. [API Endpoints](#api-endpoints)
5. [Running Tests](#running-tests)
6. [Contributing](#contributing)
7. [License](#license)
8. [Contact](#contact)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/fastapi-bookstore.git
    cd fastapi-bookstore
    ```

2. Create a virtual environment:
    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:
    - On Windows:
      ```bash
      venv\Scripts\activate
      ```
    - On macOS and Linux:
      ```bash
      source venv/bin/activate
      ```

4. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Quick Start

1. Start the FastAPI server:
    ```bash
    uvicorn books:app --reload
    ```

2. Open your browser and go to `http://127.0.0.1:8000/docs` to see the interactive API documentation (Swagger UI).

3. You can also visit `http://127.0.0.1:8000/redoc` for the ReDoc documentation.

## Project Structure

Briefly describe the main folders and files in your project:

```
fastapi-bookstore/
├── books.py              # Main entry point for the FastAPI application
├── requirements.txt      # Project dependencies
├── .gitignore            # Git ignore file
├── README.md             # Project README file
└── test/                 # Directory for unit tests
    ├── test_example.py   # Example test file
    └── __init__.py       # Initialization file for test directory
```

## API Endpoints

### Get all books
- **URL**: `/books`
- **Method**: `GET`
- **Description**: Retrieve a list of all books.
- **Response**:
    ```json
    [
        {"title": "title 1", "author": "Author 1", "category": "Math"},
        {"title": "title 2", "author": "Author 2", "category": "Science"}
    ]
    ```

### Get a book by title
- **URL**: `/books/{book_title}`
- **Method**: `GET`
- **Description**: Retrieve a book by its title.
- **Response**:
    ```json
    {"title": "title 1", "author": "Author 1", "category": "Math"}
    ```

### Get books by category
- **URL**: `/books/`
- **Method**: `GET`
- **Query Parameter**: `category` (string)
- **Description**: Retrieve books by category.
- **Response**:
    ```json
    [
        {"title": "title 2", "author": "Author 2", "category": "Science"},
        {"title": "title 3", "author": "Author 3", "category": "Science"}
    ]
    ```

### Get books by author and category
- **URL**: `/books/{book_author}/`
- **Method**: `GET`
- **Query Parameter**: `category` (string)
- **Description**: Retrieve books by author and category.
- **Response**:
    ```json
    [
        {"title": "title 2", "author": "Author 2", "category": "Science"}
    ]
    ```

### Create a new book
- **URL**: `/books/create_book`
- **Method**: `POST`
- **Body Parameters**:
    - `book_title` (string)
    - `author` (string)
    - `category` (string)
- **Description**: Create a new book.
- **Response**: Book is added to the collection.

### Update a book
- **URL**: `/books/update_book/`
- **Method**: `PUT`
- **Body Parameters**: Entire book object to update.
- **Description**: Update an existing book.
- **Response**:
    ```json
    {"message": "Book updated successfully", "book": {"title": "title 1", "author": "Author 1", "category": "Math"}}
    ```

### Delete a book
- **URL**: `/books/delete_book/{book_title}`
- **Method**: `DELETE`
- **Description**: Delete a book by its title.
- **Response**:
    ```json
    {"message": "Book deleted successfully", "book": "title 1"}
    ```

## Running Tests

1. To run tests, use the following command:
    ```bash
    pytest
    ```

2. Ensure all tests pass before making a pull request.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](https://opensource.org/license/mit) file for details.

## Contact

Contact to - [Md.Hasanuzzaman](mailto:dr.has82@gmail.com)
