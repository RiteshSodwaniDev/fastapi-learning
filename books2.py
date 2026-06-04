from typing import Optional

from fastapi import FastAPI,Path,Query
from pydantic import BaseModel,Field

app=FastAPI()





class Book:
    id: int
    title: str
    author: str
    description: str
    rating: int
    published_date: int

    def __init__(self,id,title,author,description,rating,published_date):
        self.id=id
        self.title=title
        self.author=author
        self.description=description
        self.rating=rating
        self.published_date=published_date


class BookRequest(BaseModel):
    id: Optional[int]=Field(description="Id cannot be empty",default=None)
    title:str=Field(min_length=3)
    author:str=Field(min_length=1)
    description:str=Field(min_length=1,max_length=100)
    rating:int=Field(gt=0,lt=6)
    published_date:int=Field(gt=1999,lt=2031)

    model_config = {
        "json_schema_extra":{
            "example":{
                "title":"A new Book",
                "author":"codingwithrobby",
                "description":"A new description of a book",
                "rating":5,
                "published_date":2021
            }
        }
    }






BOOKS=[
    Book(1,"Computer Sceince Pro","CodingWithRoby","A very Nice Book",5,2012),
    Book(2,"Be Fast with Fastapi","CodingWithRoby","A great Book",5,2013),
    Book(3,"Master Endpoints","CodingWithRoby","A Awesome Book",5,2012),
    Book(4,"HP1","Author 1","A very Nice Book",2,2024),
    Book(5,"HP2","Author 2","A very Nice Book",3,2012),
    Book(6,"HP3","Author 3","A very Nice Book",1,2015)
]

@app.get("/books")
async def read_all_books():
    return BOOKS

@app.get("/books/publish/")
async def filter_book_by_publishdate(published_date:  int=Query(gt=1999,lt=2031)):
    books_to_return=[]
    for book in BOOKS:
        if book.published_date==published_date:
            books_to_return.append(book)
    return books_to_return

@app.post("/create-book")
async def create_book(book_request: BookRequest):
    new_book=Book(**book_request.model_dump())
    BOOKS.append(find_book_id(new_book))


def find_book_id(book:Book):
    book.id=1 if len(BOOKS)==0 else BOOKS[-1].id+1
    return book



@app.get("/books/{book_id}")
async def read_single_book(book_id:int=Path(gt=0)):
    for book in BOOKS:
        if book.id==book_id:
            return book

@app.get("/books/")
async def filter_books_by_rating(rating:int):
    books_to_return=[]
    for book in BOOKS:
        if book.rating==rating:
            books_to_return.append(book)
    return books_to_return


@app.put("/books/update_book")
async def update_book(book:BookRequest):
    for i in range(len(BOOKS)):
        if(BOOKS[i].id==book.id):
            BOOKS[i]=book

@app.delete("/books/{book_id}")
async def delete_book(book_id:int):
    for i in range(len(BOOKS)):
        if BOOKS[i].id==book_id:
            BOOKS.pop(i)
            break


