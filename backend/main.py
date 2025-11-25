from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
from bson import ObjectId

app = FastAPI()

# Connect to MongoDB
client = MongoClient("mongodb://mongo:27017")
db = client.taskdb
tasks_collection = db.tasks

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

def task_helper(task) -> dict:
    return {
        "id": str(task["_id"]),
        "name": task["name"],
        "completed": task["completed"]
    }

# Routes
@app.get("/tasks")
def get_tasks():
    tasks = tasks_collection.find()
    return [task_helper(task) for task in tasks]

@app.post("/tasks")
def add_task(name: str):
    task = {"name": name, "completed": False}
    result = tasks_collection.insert_one(task)
    task["_id"] = result.inserted_id
    return task_helper(task)

@app.put("/tasks/{task_id}")
def update_task(task_id: str):
    task = tasks_collection.find_one({"_id": ObjectId(task_id)})
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    task["completed"] = not task["completed"]
    tasks_collection.update_one({"_id": ObjectId(task_id)}, {"$set": {"completed": task["completed"]}})
    return task_helper(task)
