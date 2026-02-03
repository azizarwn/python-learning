from pydantic import BaseModel
from typing import List, Optional

class ProductsResponse(BaseModel):
    id: int
    name: str
    price: int

class ProductsListResponse(BaseModel):
    message: str
    data: List[ProductsResponse]
    page: Optional[int] = None
    limit: Optional[int] = None

class ProductById(BaseModel):
    message: str
    data: ProductsResponse
