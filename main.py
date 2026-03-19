
from fastapi import FastAPI

items = []

app = FastAPI()

@app.get('/')
def root():
    return {"Hello": "World"}

@app.post('/items')
def create_item(item: str):
    items.append(item)
    return items

@app.get('/items')
def get_items():
    return items

@app.get('/items/{item_id}')
def get_item(item_id: int) -> str:
    item = items[item_id]
    return item
