from typing import List, Union

from fastapi import Depends, FastAPI
from pydantic import BaseModel

import redis
import psycopg2

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list = []



@app.post("/items/")
async def create_item(item: Item):
    return item

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results