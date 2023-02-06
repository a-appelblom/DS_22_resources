from typing import List
from fastapi import FastAPI
from pydantic import BaseModel


class Todo(BaseModel):
    id: int = None
    title: str
    description: str


app = FastAPI()

app.curr_id = 1
app.todos: List[Todo] = []


@app.get("/")
def root():
    return "Hello and welcome to Antons todos!"


@app.get("/todos")
def get_todos():
    return app.todos


@app.get("/todo/{id}")
def get_todo(id: int):
    return "Returns a single task with id " + str(id)


@app.post("/add_todo")
def add_todo(todo: Todo):
    print(todo)
    todo.id = app.curr_id
    app.todos.append(todo)
    app.curr_id += 1
    return "Adds a task"


@app.delete("/delete_todo/{id}")
def delete_todo(id: int):
    app.todos = list(filter(lambda x: x.id != id, app.todos))
    return True


@app.put("/update_todo/{id}")
def update_todo(id: int, new_todo: Todo):
    for todo in app.todos:
        if todo.id == id:
            todo.title = new_todo.title
            todo.description = new_todo.description
    return True
