from BookModel import Book
from BookModel_val import Book as BookVal
from typing import List
from fastapi import FastAPI,HTTPException


books_db:List[BookVal]=[]

app=FastAPI()

# 1. Get all the books
@app.get("/",response_model=List[BookVal])
def get_books():
    return books_db

# 2. Get Specific Book
@app.get("/book/{book_id}",response_model=BookVal)
def get_book(book_id:int):
    for index,books in enumerate(books_db):
        if(books.book_id==book_id):
            return books_db[index]
    raise HTTPException(status_code=404,detail="Book Not Found")

# 3. Enter new book
@app.post("/add_book",response_model=BookVal)
def add_book(new_book:BookVal):
    for book in books_db:
        if(book.book_id==new_book.book_id):
            raise HTTPException(status_code=400,detail="Book details already exists")
    books_db.append(new_book)
    return new_book

# 4. Update existing book
@app.put("/update_book/{book_id}",response_model=BookVal)
def update_book(book_id:int,updated_info:BookVal):
    for index,book in enumerate(books_db):
        if(book_id==book.book_id):
            books_db[index]=updated_info
            return {"message":"Updated successfully"}
    raise HTTPException(status_code=404,detail="Book Not Found")

# 5. Delete a book
@app.delete("/delete_book/{book_id}")
def delete_book(book_id:int):
    for index,book in enumerate(books_db):
        if(book.book_id==book_id):
            del books_db[index]
            return {"message":"Deleted successfully"}
    raise HTTPException(status_code=404,detail="Book wasn't found")
