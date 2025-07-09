
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import sqlite3
import json

app = FastAPI(title="Tesslate Generated API", version="1.0.0")

class Item(BaseModel):
    id: int = None
    title: str
    description: str = None

@app.get("/")
def read_root():
    return {"message": "Hello from Tesslate Generated App!", "status": "running"}

@app.get("/api/items", response_model=List[Item])
def get_items():
    # Simple in-memory storage for demo
    return [
        {"id": 1, "title": "Sample Item", "description": "This is a sample item"},
        {"id": 2, "title": "Another Item", "description": "Another example item"}
    ]

@app.post("/api/items", response_model=Item)
def create_item(item: Item):
    # In a real app, this would save to database
    item.id = 123  # Mock ID
    return item

@app.get("/health")
def health_check():
    return {"status": "healthy", "version": "1.0.0"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
