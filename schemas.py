from pydantic import BaseModel

class ToDoCreate(BaseModel):
    title: str

class ToDoUpdate(BaseModel):
    title: str
    is_completed: bool

class ToDoResponse(BaseModel):
    id: int
    title: str
    is_completed: bool