from fastapi import FastAPI , HTTPException
from typing import List
from models import ToDo, todos
from schemas import ToDoCreate, ToDoUpdate , ToDoResponse

app= FastAPI()

@app.get("/", response_model=str)
def read_root():
    return "Welcome to your To-Do List API!"

@app.get("/todos/",response_model=List[ToDoResponse])
def get_todos():
    return todos

@app.post("/todos/",response_model=ToDoResponse)
def create_todo(todo: ToDoCreate):
    new_todo = ToDo(title = todo.title)
    todos.append(new_todo)
    return new_todo

@app.get("/todos/{todo_id}", response_model=ToDoResponse)
def get_todo(todo_id:int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404,detail="To-Do not found")

@app.put("/todos/{todo_id}",response_model=ToDoResponse)
def update_todo(todo_id:int , todo_update: ToDoUpdate):
    for todo in todos:
        if todo.id == todo_id:
            todo.title = todo_update.title
            todo.is_completed= todo_update.is_completed
            return todo
    raise HTTPException(status_code=404,detail="To-Do not found")

@app.delete("/todos/{todo_id}",response_model=ToDoResponse)
def delete_todo(todo_id:int):
    for todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
            return todo
    raise HTTPException(status_code=404,detail="To-Do not found")