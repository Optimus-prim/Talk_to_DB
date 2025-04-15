from pymongo import MongoClient
from pprint import pprint

def connect_mongo():
    # Connect to local MongoDB
    client = MongoClient("mongodb://localhost:27017/")
    db = client['Sample_Purchaces']
    return db['User_sales']  # Use your collection name

def print_raw_data(collection, limit=10):
    print(f"\n🔍 Showing first {limit} documents from MongoDB:\n")
    for doc in collection.find().limit(limit):
        pprint(doc)

if __name__ == "__main__":
    collection = connect_mongo()
    print_raw_data(collection)
