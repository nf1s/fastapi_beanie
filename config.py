import os

MONGO_URI: str = os.getenv(
    "MONGO_URI",
     "mongodb://localhost:27017",
)

MONGO_DB_NAME: str = os.getenv(
    "MONGO_DB_NAME",
     "fastapi-tasks",
)

