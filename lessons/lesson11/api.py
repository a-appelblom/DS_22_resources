from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return "Hello and welcome to Antons todos!"


@app.get("/todos")
def get_todos():
    return "Returns a list of all the available tasks"


@app.get("/todo/{id}")
def get_todo(id: int):
    return "Returns a single task with id " + str(id)


@app.post("/add_todo")
def add_todo(todo):
    return "Adds a task"


@app.delete("/delete_todo/{id}")
def delete_todo(id: int):
    return "Deletes a task with id: " + str(id)


@app.put("/update_todo/{id}")
def update_todo(id: int):
    return "Will update task with id " + str(id)
