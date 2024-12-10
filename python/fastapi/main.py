from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class Pessoa(BaseModel):
    nome:str
    idade : int
    altura: float


@app.get('/')
def index():
    """Mensagem de boas vindas

    Returns:
        str: mensagem
    """
    return {"Messagem":"Ola fastApi"}


@app.post('/pessoa/')
def cria_pessoa(pessoa:Pessoa):
    return pessoa

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000)