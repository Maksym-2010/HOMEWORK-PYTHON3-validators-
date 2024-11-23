from typing import Optional
from pydantic import BaseModel


class ToDoBase(BaseModel):
    title: str
    description: str


class ToDoCreate(ToDoBase):
    pass

class ToDoUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    completed: Optional[bool]

class ToDoResponse(ToDoBase):
    id: int
    completed: bool

    class Config:
        orm_mode = True
