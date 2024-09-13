"""This is main module
"""

from datetime import date
from fastapi import FastAPI
from api.models import BookResponse, BookRequest

app = FastAPI()


@app.get("/books", response_model=list[BookResponse])
def get_all_books():
    responses = []
    responses.append(
        BookResponse(
            id="1001",
            title="Dopamine Detox",
            author="Thibaut Meurissee",
            isbn="1234567",
            published_date=date.today(),
        )
    )
    return responses


@app.post("/books", response_model=BookResponse)
def create_book(request: BookRequest):
    return BookResponse(
        id="1002",
        title=request.title,
        author=request.author,
        isbn=request.isbn,
        published_date=request.published_date,
    )
