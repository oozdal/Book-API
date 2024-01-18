from fastapi import FastAPI, Body
from pydantic import BaseModel

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
    id: int
    title: str
    author: str
    description: str
    rating: int



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
    BOOKS.append(new_book)
