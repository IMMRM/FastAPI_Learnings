from fastapi import FastAPI
from pydantic import BaseModel
from dataclasses import dataclass

class User(BaseModel):
    name: str
    age: int

@dataclass
class NewUser:
    name: str
    age: int

app=FastAPI()

@app.get("/",response_model=User)
def display():
    return User(name="Alice",age="t34")

@app.get("/user",response_model=NewUser)
def new_display():
    return NewUser(name="Alice",age="t12")