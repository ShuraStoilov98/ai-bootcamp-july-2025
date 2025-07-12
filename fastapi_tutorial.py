from fastapi import FastAPI, HTTPException

items = []

app = FastAPI()  # <- this must exist at top-level (not inside a function)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI Tutorial"}

@app.post("/items/")
def create_item(item: str):
    items.append(item)
    return item

@app.get("/items/{item_id}")
def read_item(item_id: int) -> str:
    if item_id < 0 or item_id >= len(items):
        raise HTTPException(status_code=404, detail="Item not found")
    else:
        return items[item_id]
    

# Raising errors via HTTP response status codes - standard HTTP error codes
