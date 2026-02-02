from pydantic import BaseModel
from typing import List

class ProductsResponse(BaseModel):
    id: int
    name: str
    price: int

class ProductsListResponse(BaseModel):
    message: str
    data: List[ProductsResponse]
    page: int

class ProductById(BaseModel):
    message: str
    data: ProductsResponse
