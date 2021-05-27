
from flask_pymongo import pymongo
import os

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

client = pymongo.MongoClient(
    "mongodb+srv://{DB_USER}:{DB_PASSWORD}@cluster0.qobtq.mongodb.net/{DB_NAME}?retryWrites=true&w=majority"
)