from fastapi import FastAPI

app = FastAPI(
    # docs_url=None,  # here to hide docs path
    redoc_url=None,
)

@app.get(path="/hello")
def say_hello():
    return {"message": "Hello, World!"}