from fastapi import FastAPI, HTTPException
from test import Book, get_all_books, get_book_by_id
from typing import List

app = FastAPI()

# Root endpoint
# Method: GET
# Path: /
# Response: Welcome message
@app.get("/")
async def root():
    """
    Root endpoint that provides API welcome message
    Returns:
        dict: Welcome message
    """
    return {"message": "Welcome to Book API"}

# Books list endpoint
# Method: GET
# Path: /books
# Response: List of all books
@app.get("/books", response_model=List[Book])
async def get_books():
    """
    Retrieve all books from the database
    Returns:
        List[Book]: List of all book objects
    """
    return get_all_books()

# Single book endpoint
# Method: GET
# Path: /books/{book_id}
# Parameters: book_id (int)
# Response: Single book or 404
@app.get("/books/{book_id}", response_model=Book)
async def get_book(book_id: int):
    """
    Retrieve a specific book by ID
    Args:
        book_id (int): Unique identifier of the book
    Returns:
        Book: Book object if found
    Raises:
        HTTPException: 404 if book not found
    """
    book = get_book_by_id(book_id)
    if book is None:
        raise HTTPException(status_code=404, detail=f"Book with id {book_id} not found")
    return book