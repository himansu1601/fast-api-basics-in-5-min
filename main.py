from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


class Sum(BaseModel):
    num1: int
    num2: int


@app.get("/")
def home_path():
    return {"Hello World"}


@app.post("/sum")
def sum(sum: Sum):
    return f'The sum of {sum.num1} and {sum.num2} is {sum.num1+sum.num2}'


@app.get("/sum/{x}/{y}")
def add_nums(x: int, y: int):
    return x+y


@app.get("/items/{item_id}")
def item_path(item_id: int):
    return {"item_id": item_id}


@app.get("/items_string/{item_id}")
def item_string_path(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
