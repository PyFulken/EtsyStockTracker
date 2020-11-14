import tkinter
import json_handler
from tkinter import *
from tkinter import ttk

#First Data Load
stock_data = json_handler.load_data()

#GUI
root = Tk()

#Root Window Management

root.title("Monitoring Windows")
root.maxsize(height=root.winfo_screenheight() - 100)
root.resizable(width="False", height="False")
title_label = Label(root, text="Stock Tracker", font = "Helvetica 16 bold italic")
title_label.pack(side="top")


#Current Stock
stock_frame = Frame(root)
stock_frame.pack(side="left")
row_manager = 0

for key, value in stock_data.items():
    stock_label = Label(stock_frame, relief="solid", borderwidth=1, background="white", width=20, height=1, anchor="w")
    stock_label.config(text=key)
    stock_label.grid(row=row_manager, column=0, ipadx=10, padx=10, pady=3)
    stock_amount = Label(stock_frame, relief="solid", borderwidth=1, background="white", width=6, height=1, anchor="e")
    stock_amount.config(text=value)
    stock_amount.grid(row=row_manager, column=1, ipadx=10, padx=10, pady=3)

    row_manager += 1

root.mainloop()