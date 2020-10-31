import tkinter
from tkinter import *
from tkinter import ttk
from MongoDB import *

import requests

#Mongo Connection
connect = connect_to_db()

# add_stock(connect["prints"], "Stamps", 10)
all_items_amounts = get_all_stocks(connect)

#GUI
root = Tk()

#Root Window Management
root.title("Monitoring Windows")
screen_height = root.winfo_screenheight() - 100
screen_width = root.winfo_screenwidth() - 100
root.geometry("{}x{}".format(screen_width,screen_height))
root.resizable(width="False", height="False")

#Login page

#Current Stock
for item in all_items_amounts:
    item_label = ttk.Label(root, justify="center", font="arial 10 bold", wrap=350)
    item_label.pack()
    item_label.config(text="{}'s current stock: {}".format(item[0], item[1]))
root.mainloop()