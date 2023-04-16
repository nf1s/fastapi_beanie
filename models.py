from beanie import Document, Indexed
from pydantic import BaseModel


class Task(Document, BaseModel):
    class Settings:
        name = "tasks"

    id: str
    title: str
    description: str
    is_done: bool = False
