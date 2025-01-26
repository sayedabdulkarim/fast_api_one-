from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

class Book(BaseModel):
    id: int
    title: str
    author: str
    year: Optional[int] = None

app = FastAPI()

# add a get route to the app
@app.get("/")
async def root():
    return {"message": "Welcome to Book API"}


# Sample data
books = [
    Book(id=1, title="The Great Gatsby", author="F. Scott Fitzgerald", year=1925),
    Book(id=2, title="1984", author="George Orwell", year=1949)
]

@app.get("/books", response_model=List[Book])
async def get_books():
    """
    Retrieve all books from the database
    """
    return books

@app.get("/books/{book_id}", response_model=Book)
async def get_book_by_id(book_id: int):
    """
    Get a book by its ID
    
    Args:
        book_id (int): The ID of the book to retrieve
        
    Returns:
        Book: The book object if found
        
    Raises:
        HTTPException: If book is not found
    """
    book = next((book for book in books if book.id == book_id), None)
    if book is None:
        raise HTTPException(status_code=404, detail=f"Book with id {book_id} not found")
    return book