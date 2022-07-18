import pymongo
from pymongo import MongoClient

import info_mongodb, gather

# Implementar sistema de login
# import login

data = gather.data_gather()

emotion = gather.data_gather()

client = MongoClient(info_mongodb.creds)


def send():
    db = client.umirror
    collection = db.emotions

    post_id = collection.insert_one(data).inserted_id

    print(f"[+]Post ID: {post_id}")
    # print(f"[+]Insertion ID: {}")
    # print(f"[+]ID unico: {}")
