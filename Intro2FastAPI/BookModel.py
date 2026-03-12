from pydantic import BaseModel

class Book(BaseModel):
    book_id:int
    book_name:str
    book_genre:str
    book_cost:float