#!/usr/bin/env python3
import redis

# Create a connection to the Redis server
redis_client = redis.StrictRedis(host='redis', port=6379, db=0, decode_responses=True)

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Product(BaseModel):
    name: str
    price: float
    quantity: int

@app.post("/products/")
def add_product(product: Product):
    # Store product in Redis
    redis_client.set(product.name, f"{product.price},{product.quantity}")
    return {"message": "Product added successfully!"}

@app.get("/products/{name}")
def get_product(name: str):
    product_data = redis_client.get(name)
    if product_data:
        price, quantity = product_data.split(',')
        return {"name": name, "price": float(price), "quantity": int(quantity)}
    return {"error": "Product not found"}
