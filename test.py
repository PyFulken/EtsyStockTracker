import tkinter
from tkinter import *
from tkinter import ttk
from MongoDB import *
from PIL import ImageTk,Image
from functools import partial
import requests

#Mongo Connection
connect = connect_to_db()

# add_stock(connect["prints"], "Stamps", 10)
all_items_amounts = get_all_stocks(connect)

def getvalue(entry_var):
    amount = entry_var.get()
    return amount

def printstuff(n, m, b):
    print(n)
    print(m)
    print(b)
#GUI
root = Tk()

#Root Window Management
root.title("Monitoring Windows")

background = PhotoImage(file = "EtsyStockTracker/background.png")
background_label = Label(root, image=background)
background_label.place(x=0, y=0, relwidth=1, relheight=1)


screen_height = root.winfo_screenheight() - 400
screen_width = root.winfo_screenwidth() - 800
root.geometry("{}x{}".format(screen_width,screen_height))
root.resizable(width="False", height="False")

#Login page


#Current Stock
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

    add_button = ttk.Button(root, command=partial(printstuff, item[0], item[1], amount_entry.get()), text="Add")
    add_button.grid(row=item_iterator, column=4, padx=10, pady=5)
    
    remve_partial = partial(remove_stock, item[0], item[1], amount_entry.get)
    remve_button = ttk.Button(root, command=partial(printstuff, item[0], item[1], amount_entry.get()), text="Remove")
    remve_button.grid(row=item_iterator, column=5, padx=10, pady=5)

    item_iterator +=1
root.mainloop()