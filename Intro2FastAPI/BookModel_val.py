from pydantic import BaseModel,Field
from typing import Optional

class Book(BaseModel):
    book_id:int = Field(...,gt=0)
    book_name:str = Field(...,min_length=2, max_length=100)
    book_genre:str = Field(...,min_length=2, max_length=50)
    book_cost:Optional[float] = Field(None,gt=0)