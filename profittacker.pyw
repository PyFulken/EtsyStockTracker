import tkinter
import datetime
import json_handler
from tkinter import *
from tkinter import ttk

#First Data Load
sales_data = json_handler.load_sales_data()

#GUI
root = Tk()

#Root Window Management

root.title("EZ Stock Tracker 3000-ninator")
root.maxsize(height=root.winfo_screenheight() - 100)
root.resizable(width="False", height="False")
title_label = Label(root, text="Sales Tracker", font = "Helvetica 16 bold italic")
title_label.pack(side="top")

time_label = Label(root, text=f"Sales for {datetime.datetime.now().strftime('%B')} {datetime.datetime.now().strftime('%Y')}", font = "Helvetica 12 bold italic")
time_label.pack(side="top")

#Current Stock
top_frame = Frame(root)
top_frame.pack()

name_label = Label(top_frame,  font = "Helvetica 12 bold italic", text="Product")
name_label.grid(row=0, column=0, ipadx=10, padx=10, pady=3)

sales_label = Label(top_frame,  font = "Helvetica 12 bold italic", text="Sales")
sales_label.grid(row=0, column=1, ipadx=10, padx=10, pady=3)

profit_label = Label(top_frame,  font = "Helvetica 12 bold italic", text="Profit")
profit_label.grid(row=0, column=2, ipadx=10, padx=10, pady=3)

row_iterator = 1

for key in sales_data.keys():
    item_name = Label(top_frame, relief="solid", borderwidth=1, background="white", width=15, height=1, anchor="w", text=key)
    item_name.grid(row=row_iterator, column=0, ipadx=10, padx=10, pady=3)

    sales_month = sales_data[key]["sales"][datetime.datetime.now().strftime("%Y")][datetime.datetime.now().strftime("%b")]
    
    item_sales = Label(top_frame, relief="solid", borderwidth=1, background="white", width=15, height=1, anchor="w", text=sales_month)
    item_sales.grid(row=row_iterator, column=1, ipadx=10, padx=10, pady=3)

    profit = sales_month * sales_data[key]["profit"]
    profit_label = Label(top_frame, relief="solid", borderwidth=1, background="white", width=15, height=1, anchor="w", text=f"{profit}€")
    profit_label.grid(row=row_iterator, column=2, ipadx=10, padx=10, pady=3)



root.mainloop()