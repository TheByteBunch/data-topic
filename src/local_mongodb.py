from dotenv import load_dotenv
import os
from pymongo import MongoClient

load_dotenv()

CONNECTION = os.getenv("MONGO_DB_CONNECTION")
client = MongoClient(CONNECTION)
print(client)
db = client["db_mongo_test"]
collection = db["db_sample"]
post = {
    "author": "asdjsajdd"
}

collection.insert_one(post)