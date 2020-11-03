import pymongo
import os
from dotenv import load_dotenv

load_dotenv("EtsyStockTracker/config.env")

def connect_to_db():
    """
    Connects to the remote MongoDB database

    Returns a Dictionary with the collection objects, to be used to manipulate the database.
    """
    try:
        mongo = pymongo.MongoClient(os.environ.get("MONGO_URL"))
        db = mongo[os.environ.get("DATABASE")]
        collection_dict = {}
        collection_dict["prints"] = db["print"]
        collection_dict["stickers"] = db["sticker"]
        
        return collection_dict
    except:
        print("Oh no!")

def get_all_stocks(collection_dict):

    try:
        item_list = []
        for collection in collection_dict.values():
            for item in collection.find():
                formatted_item = [collection, item["name"], item["amount"]]
                item_list.append(formatted_item)
        return item_list
    except:
        print("Get! Oh no!")

def add_stock(collection, name, amount):
    """
    Adds the 'amount' argument to the 'amount' field of the specified 'name' entry present in 'collection'.
    
    collection: A collection object stored in the collection_dict.
    name: String, name of the entry to manipulate.
    amount: Int, number to increment by.
    """
    try:
        query = { "name": { "$regex": "{}".format(name) } }
        value = collection.find_one(query)
        total = amount + value["amount"]
        values = { "$set": { "amount": total } }
        entry = collection.update_one(value, values)
    except:
        return print("Error has occured")

def remove_stock(collection, name, amount):
    """
    Removes the 'amount' argument to the 'amount' field of the specified 'name' entry present in 'collection'.
    
    collection: A collection object stored in the collection_dict.
    name: String, name of the entry to manipulate.
    amount: Int, number to decrement by.
    """
    try:
        query = { "name": { "$regex": "{}".format(name) } }
        value = collection.find_one(query)
        total = amount - value["amount"]
        values = { "$set": { "amount": total } }
        entry = collection.update_one(value, values)
    except:
        return print("Error has occured")