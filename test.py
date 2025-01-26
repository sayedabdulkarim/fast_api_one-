from typing import List, Optional
from pydantic import BaseModel

class Book(BaseModel):
    id: int
    title: str
    author: str
    year: Optional[int] = None

# Sample data
books = [
    Book(id=1, title="The Great Gatsby", author="F. Scott Fitzgerald", year=1925),
    Book(id=2, title="1984", author="George Orwell", year=1949)
]

def get_all_books() -> List[Book]:
    """Get all books from the database"""
    return books

def get_book_by_id(book_id: int) -> Optional[Book]:
    """Get a book by its ID"""
    return next((book for book in books if book.id == book_id), None)

def generateName(firstname: str, lastname: str) -> str:
    """Generate full name"""
    return firstname.capitalize() + " " + lastname


name =  generateName('asd', "doe")

print(name)