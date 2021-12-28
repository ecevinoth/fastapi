from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

todos = {}

# GET [SELECT RECORD]


class task(BaseModel):
    task: str


@app.get("/", tags=['Root'])
async def root() -> dict:
    return {"hello ": "World"}


@app.get("/todo", tags=["Todo"])
async def todo() -> dict:
    return {"data": todos}


# POST [NEW RECORD]
@app.post("/todo/{id}", tags=['Todo'])
async def todo(id: str, tasks: task) -> dict:
    if id in todos:
        return {"error": " exist already"}
    todos[id] = tasks
    return {"result": "successfully added task to todos."}


# PUT [UPDATE EXISTING RECORD]
@app.put("/todo/{id}", tags=['Todo'])
async def todo(id: str, tasks: task) -> dict:
    if id in todos:
        todos[id] = tasks
        return {"result": "updated successfully"}
    return {"error": "not able to find the todo ID"}

# DELETE [DELETE RECORD]


@app.delete("/todo/{id}", tags=['Todo'])
async def todo(id: str) -> dict:
    if id in todos:
        del todos[id]
        return {"result": "deleted successfully"}
    return {"error": "not able to find the todo ID"}
