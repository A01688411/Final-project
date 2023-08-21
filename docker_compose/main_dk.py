import logging
from typing import Optional
from fastapi import FastAPI


logging.basicConfig(filename='api_logs.log', level=logging.DEBUG,
                    format='%(asctime)s:%(name)s:%(module)s:%(levelname)s:%(message)s')

app = FastAPI()

@app.get("/")
def read_root():
    logging.info("Hello World!")
    return {"Hello": "World"}
    
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    logging.debug(f"item_id: {item_id}")
    return {"item_id": item_id, "q": q}