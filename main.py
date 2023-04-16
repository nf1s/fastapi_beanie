from typing import List

from fastapi import FastAPI, HTTPException

import config
from database import MongoDB
from models import Task

app = FastAPI()


@app.on_event("startup")
async def on_startup():
    await MongoDB.init(config.MONGO_URI, config.MONGO_DB_NAME)


@app.post("/tasks", response_model=Task)
async def create_task(task: Task):
    await task.insert()
    return task


@app.get("/tasks", response_model=List[Task])
async def read_tasks():
    tasks = await Task.find_all().to_list()
    return tasks


@app.get("/tasks/{task_id}", response_model=Task)
async def read_task(task_id: str):
    task = await Task.find_one({"id": task_id})
    if not task:
        raise HTTPException(status_code=404, detail="Task")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
