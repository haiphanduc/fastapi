from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello")
async def say_hello():
    return {"message": f"Hello Group"}
