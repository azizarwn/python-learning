from itertools import product
from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference
from src.day_3.app.modules.products.serializer import ProductById, ProductsListResponse, ProductsResponse

# script to run localhost
# uv run uvicorn main:app--reload

app = FastAPI(
    # docs_url=None,  # here to hide docs path
    redoc_url=None,
)

@app.get(path="/hello")
def say_hello():
    return {"message": "Hello, World!"}

@app.get(path="/products", tags=["products"], response_model=ProductsListResponse)
def get_products(page: int = None, limit: int = None):
     # Mock data (expanded for pagination testing)
    product_list = [
        ProductsResponse(id=1, name="Product 1", price=100),
        ProductsResponse(id=2, name="Product 2", price=400),
        ProductsResponse(id=3, name="Product 3", price=400),
        ProductsResponse(id=4, name="Product 4", price=400),
        ProductsResponse(id=5, name="Product 5", price=400),
    ]
    # ✅ SINGLE LOGIC PATH: Paginate ONLY if BOTH params provided
    if page is not None and limit is not None:
        skip = (page - 1) * limit
        paginated = product_list[skip:skip + limit]
        return ProductsListResponse(
            message=f"Page {page} retrieved successfully",
            data=paginated,
            page=page,
            limit=limit
        )
    else:
        return ProductsListResponse(
        message="All products retrieved successfully",
        data=product_list
        # page/limit omitted → defaults to None (Pydantic handles it)
    )



@app.get(path="/products/{product_id}", tags=["products"], response_model=ProductById)
def get_product_by_id(product_id: int):
    product = ProductsResponse(id=product_id, name=f"Product {product_id}", price=100)
    return ProductById(message="Product by Id success", data=product)

@app.post(path="/products", tags=["products"])
def create_product():
    return {
        "product": {}
    }

@app.patch(path="/products/{id}", tags=["products"])
def update_product_by_id():
    return {
        "product": {}
    }

@app.delete(path="/products/{id}", tags=["products"])
def delete_product_by_id():
    return {
        "product": None
    }


# documentation in scalar 
@app.get(path="/scalar")
def scalar_doc():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
    )