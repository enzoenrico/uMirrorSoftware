import pymongo
from pymongo import MongoClient

import gather

# Implementar sistema de login
# import login

emotion = gather.data_gather()

client = MongoClient()

def send():
    db = client.umirror
    collection = db.emotions

    data = gather.data_gather()

    post_id = collection.insert_one(data).inserted_id

    print(f"[+]Post ID: {post_id}")
    # print(f"[+]Insertion ID: {}")
    # print(f"[+]ID unico: {}")
