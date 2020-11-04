import pymongo
import os
from dotenv import load_dotenv
from tkinter import *
from tkinter import ttk
from functools import partial

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
        total = int(amount.get()) + value["amount"]
        values = { "$set": { "amount": total } }
        entry = collection.update_one(value, values)
    except:
        return print("Error has occured")

def remove_stock(collection, name, amount):
    """
    Removes the 'amount' argument to the 'amount' field of the specified 'name' entry present in 'collection'.
    
    collection: A collection object stored in the collection_dict.
    name: String, name of the entry to manipulate.
    amount: The entry box variable.
    """
    try:
        query = { "name": { "$regex": "{}".format(name) } }
        value = collection.find_one(query)
        total = value["amount"] - int(amount.get())
        values = { "$set": { "amount": total } }
        entry = collection.update_one(value, values)
    except:
        return print("Error has occured")

def populate_stock(root, all_items_amounts):
    item_iterator=0
    for item in all_items_amounts:
        item_label = ttk.Label(root, justify="center", font="arial 10 bold", wrap=350, background="#f1bcee", relief="ridge", borderwidth="1px", width=30 )
        item_label.grid(row=item_iterator, column=0, padx=10, pady=5, sticky="WENS")
        item_label.config(text="{}'s current stock:".format(item[1]))

        item_amount_label = ttk.Label(root, justify="center", font="arial 10 bold", wrap=350, background="#f1bcee", relief="ridge", borderwidth="1px", width=10 )
        item_amount_label.grid(row=item_iterator, column=2, padx=10, pady=5)
        item_amount_label.config(text="{}".format(item[2]))

        amount_entry = ttk.Entry(root, width=10)
        amount_entry.grid(row=item_iterator, column=3, padx=10, pady=5)

        add_button = ttk.Button(root, command=partial(add_stock, item[0], item[1], amount_entry), text="Add")
        add_button.grid(row=item_iterator, column=4, padx=10, pady=5)
        
        remove_button = ttk.Button(root, command=partial(remove_stock, item[0], item[1], amount_entry), text="Remove")
        remove_button.grid(row=item_iterator, column=5, padx=10, pady=5)

        item_iterator +=1

def repopulate_stock(root, frame, connection):
    frame.destroy()
    frame = ttk.Label(root)
    frame.pack()
    all_items_amounts = get_all_stocks(connection)
    item_iterator=0
    for item in all_items_amounts:
        item_label = ttk.Label(frame, justify="center", font="arial 10 bold", wrap=350, background="#f1bcee", relief="ridge", borderwidth="1px", width=30 )
        item_label.grid(row=item_iterator, column=0, padx=10, pady=5, sticky="WENS")
        item_label.config(text="{}'s current stock:".format(item[1]))

        item_amount_label = ttk.Label(frame, justify="center", font="arial 10 bold", wrap=350, background="#f1bcee", relief="ridge", borderwidth="1px", width=10 )
        item_amount_label.grid(row=item_iterator, column=2, padx=10, pady=5)
        item_amount_label.config(text="{}".format(item[2]))

        amount_entry = ttk.Entry(frame, width=10)
        amount_entry.grid(row=item_iterator, column=3, padx=10, pady=5)

        add_button = ttk.Button(frame, command=partial(add_stock, item[0], item[1], amount_entry), text="Add")
        add_button.grid(row=item_iterator, column=4, padx=10, pady=5)
        
        remove_button = ttk.Button(frame, command=partial(remove_stock, item[0], item[1], amount_entry), text="Remove")
        remove_button.grid(row=item_iterator, column=5, padx=10, pady=5)

        item_iterator +=1