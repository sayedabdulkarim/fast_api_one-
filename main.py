from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

class Book(BaseModel):
    id: int
    title: str
    author: str
    year: Optional[int] = None

app = FastAPI()

## test
@app.get("/")
def index():
    return "Hello World"

@app.get("/about")
def about():
    return "About Page"

# Sample data
books = [
    Book(id=1, title="The Great Gatsby", author="F. Scott Fitzgerald", year=1925),
    Book(id=2, title="1984", author="George Orwell", year=1949)
]

# @app.get("/")
# async def root():
#     return {"message": "Welcome to Book API"}

# @app.get("/books", response_model=List[Book])
# async def get_books():
#     """
#     Retrieve all books from the database
#     """
#     return books