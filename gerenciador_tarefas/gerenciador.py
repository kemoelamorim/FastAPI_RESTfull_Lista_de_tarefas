from fastapi import FastAPI

app = FastAPI()

TAREFAS = []

@app.get("/")
def welcome():
    return "{'Welcome':'Very Good'}"

@app.get("/tarefas")
def listar_tarefas():
    return TAREFAS