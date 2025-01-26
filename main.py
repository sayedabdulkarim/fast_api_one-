from fastapi import FastAPI, HTTPException
from test import Book, get_all_books, get_book_by_id
from typing import List

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to Book API"}

@app.get("/books", response_model=List[Book])
async def get_books():
    """Retrieve all books from the database"""
    return get_all_books()

@app.get("/books/{book_id}", response_model=Book)
async def get_book(book_id: int):
    """Retrieve a specific book by ID"""
    book = get_book_by_id(book_id)
    if book is None:
        raise HTTPException(status_code=404, detail=f"Book with id {book_id} not found")
    return book