import tkinter
import json_handler
from tkinter import *
from tkinter import ttk

#First Data Load
stock_data = json_handler.load_stock_data()

def populate_window(stock_data):
    row_manager = 0
    entry_box_variables = {}
    item_amounts = {}
    stock_amount_labels = {}
    if len(item_amounts) == 0:
        for key, value in stock_data.items():
            entry_box_variables[row_manager] = StringVar()
            stock_label = Label(stock_frame, relief="solid", borderwidth=1, background="white", width=20, height=1, anchor="w")
            stock_label.config(text=key)
            stock_label.grid(row=row_manager, column=0, ipadx=10, padx=10, pady=3)

            item_amounts[key] = StringVar()
            item_amounts[key].set(value)
            stock_amount_labels[key] = Label(stock_frame, relief="solid", borderwidth=1, background="white", width=6, height=1, anchor="e", text=item_amounts[key].get())
            stock_amount_labels[key].grid(row=row_manager, column=1, ipadx=10, padx=10, pady=3)
            amount_label= Entry(stock_frame, relief="solid", borderwidth=1, background="white", width=6, textvariable=entry_box_variables[row_manager])
            amount_label.grid(row=row_manager, column=2, ipadx=10, padx=10, pady=3)

            row_manager += 1



#GUI
root = Tk()

#Root Window Management

root.title("EZ Stock Tracker 3000-ninator")
root.maxsize(height=root.winfo_screenheight() - 100)
root.resizable(width="False", height="False")
title_label = Label(root, text="Sales Tracker", font = "Helvetica 16 bold italic")
title_label.pack(side="top")

#Current Stock
stock_frame = Frame(root)
stock_frame.pack()

root.mainloop()