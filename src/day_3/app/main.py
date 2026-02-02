from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference
from modules.products.serializer import ProductById, ProductsResponse, ProductsListResponse

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
def get_products(page: int):
    product_list = [
        ProductsResponse(id=1, name="Product 1", price=100),
        ProductsResponse(id=2, name="Product 2", price=400),
    ]
    if page:
        return ProductsListResponse(message="Product List success", data=product_list, page=page)
    else:
        return ProductsListResponse(message="Product List success", data=product_list)


@app.get(path="/products/{product_id}", tags=["products"], response_model=ProductById)
def get_product_by_id(product_id: int):
    product = ProductsResponse(id=product_id, name=f"Product {product_id}", price=100)
    return ProductById(message="Product by Id success", data=product)


# documentation in scalar 
@app.get(path="/scalar")
def scalar_doc():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
    )