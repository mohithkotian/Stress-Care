import os
from pathlib import Path

from dotenv import load_dotenv
from pymongo import MongoClient

# Load the backend-local environment file when running from any working directory.
load_dotenv(Path(__file__).resolve().parents[1] / ".env")

MONGO_URI = os.getenv("MONGO_URI")
if not MONGO_URI:
    raise RuntimeError("MONGO_URI is required; configure it in backend/.env or the process environment")

DB_NAME = os.getenv("DB_NAME", "stress_care")

client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
db = client[DB_NAME]
