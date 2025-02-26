from fastapi import FastAPI
from fast_zero.schemas import Message
from http import HTTPStatus

from fast_zero.routers import users,auth
app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router)

@app.get("/", status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {"message": "Hello world"}


