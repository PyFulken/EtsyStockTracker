import tkinter
from tkinter import *
from tkinter import ttk
from MongoDB import *
from PIL import ImageTk,Image
import requests
from functools import partial

#Mongo Connection
connect = connect_to_db()
all_items_amounts = get_all_stocks(connect)
# add_stock(connect["prints"], "Stamps", 10)

#GUI
root = Tk()

#Root Window Management
root.title("Monitoring Windows")

background = PhotoImage(file = "EtsyStockTracker/background.png")
background_label = Label(root, image=background)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


screen_height = root.winfo_screenheight() - 700
screen_width = root.winfo_screenwidth() - 1000
root.geometry("{}x{}".format(screen_width,screen_height))
root.resizable(width="False", height="False")

#Login page


#Current Stock
stock_label_parent = ttk.Label(root)
stock_label_parent.pack()
stock_label = ttk.Label(stock_label_parent)
stock_label.pack()
populate_stock(stock_label, all_items_amounts)

refresh_partial = partial(repopulate_stock, stock_label_parent, stock_label, connect)
refresh_button = ttk.Button(root, command=refresh_partial, text="Refresh")
refresh_button.pack()

root.mainloop()