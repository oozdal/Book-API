from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional


app = FastAPI()


class Book:
    id: int
    title: str
    author: str
    description: str
    rating: str

    
    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating


class BookRequest(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=6)


BOOKS = [
    Book(1, 'Computer Science Pro', 'CodingWithOzer', 'A very nice book!', 5),
    Book(2, 'Be Fast with FastAPI', 'CodingWithOzer', 'A great book!', 5),
    Book(3, 'Master Endpoints', 'CodingWithOzer', 'A awesome book!', 5),
    Book(4, 'HP1', 'Author1', 'A very nice book!', 2),
    Book(5, 'HP2', 'Author2', 'A very nice book!', 3),
    Book(6, 'HP3', 'Author3', 'A very nice book!', 1)
]


@app.get("/books")
async def read_all_books():
    return BOOKS


@app.post("/create_book")
async def create_book(book_request: BookRequest):
    new_book =  Book(**book_request.dict())
    BOOKS.append(find_book_id(new_book))


def find_book_id(book: Book):
    book.id = 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    return book