import pymongo

def connect_to_db():
    """
    Connects to the remote MongoDB database

    Returns a Dictionary with the collection objects, to be used to manipulate the database.
    """
    mongo = pymongo.MongoClient("mongodb+srv://root:Anna1Anna2Anna3@stocktracker.qgcja.mongodb.net/stock?retryWrites=true&w=majority")
    db = mongo["stock"]
    collection_dict = {}
    collection_dict["prints"] = db["print"]
    collection_dict["stickers"] = db["sticker"]
    
    return collection_dict

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