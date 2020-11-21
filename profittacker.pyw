import tkinter
import datetime
import json_handler
from tkinter import *
from tkinter import ttk

#First Data Load
sales_data = json_handler.load_sales_data()

#Button Functions

def add_sale(item, amount, data):
    data[item]["sales"][datetime.datetime.now().strftime("%Y")][datetime.datetime.now().strftime("%b")] += amount
    json_handler.change_sales_data(data)

def add_item(item, profit, data):
    data[item] = {"profit": profit, "sales": {f"{datetime.datetime.now().strftime('%Y')}": {"Jan": 0, "Feb": 0, "Mar": 0, "Apr": 0, "May": 0, "Jun": 0, "Jul": 0, "Aug": 0, "Sep": 0, "Oct": 0, "Nov": 0, "Dec": 0}}}
    json_handler.change_sales_data(data)


#GUI
root = Tk()


#Root Window Management

root.title("Sales Tracker")
root.maxsize(height=root.winfo_screenheight() - 100)
root.minsize(550,0)
root.resizable(width="False", height="False")
title_label = Label(root, text="Sales Tracker", font = "Helvetica 16 bold italic")
title_label.pack(side="top")

time_label = Label(root, text=f"Sales for {datetime.datetime.now().strftime('%B')} {datetime.datetime.now().strftime('%Y')}", font = "Helvetica 12 bold italic")
time_label.pack(side="top")


#Current Sales

top_frame = Frame(root)
top_frame.pack()

name_label = Label(top_frame,  font = "Helvetica 12 bold italic", text="Product")
name_label.grid(row=0, column=0, ipadx=10, padx=10, pady=3)

sales_label = Label(top_frame,  font = "Helvetica 12 bold italic", text="Sales")
sales_label.grid(row=0, column=1, ipadx=10, padx=10, pady=3)

profit_label = Label(top_frame,  font = "Helvetica 12 bold italic", text="Profit")
profit_label.grid(row=0, column=2, ipadx=10, padx=10, pady=3)

total_profit = 0
row_iterator = 1

for key in sales_data.keys():
    item_name = Label(top_frame, relief="solid", borderwidth=1, background="white", width=15, height=1, text=key)
    item_name.grid(row=row_iterator, column=0, ipadx=10, padx=10, pady=3)

    sales_month = sales_data[key]["sales"][datetime.datetime.now().strftime("%Y")][datetime.datetime.now().strftime("%b")]
    
    item_sales = Label(top_frame, relief="solid", borderwidth=1, background="white", width=15, height=1, text=sales_month)
    item_sales.grid(row=row_iterator, column=1, ipadx=10, padx=10, pady=3)

    profit = sales_month * sales_data[key]["profit"]
    profit_label = Label(top_frame, relief="solid", borderwidth=1, background="white", width=15, height=1, text=f"{profit} €")
    profit_label.grid(row=row_iterator, column=2, ipadx=10, padx=10, pady=3)

    row_iterator += 1
    total_profit += profit


#Sales Addition:

middle_frame = Frame(root)
middle_frame.pack(padx=50, pady=10)

new_sale_label = Label(middle_frame, text="Add Sale:", font = "Helvetica 12 bold italic")
new_sale_label.pack(side="left", ipadx=10, padx=10, pady=3)

new_sale_name_var = StringVar() 
new_sale_name_var.set("Choose an Item")
new_sale_name = OptionMenu(middle_frame, new_sale_name_var, *sales_data.keys())
new_sale_name.pack(side="left", ipadx=10, padx=10, pady=3)

new_sale_amount_var = StringVar() 
new_sale_amount_var.set("0")
new_sale_amount = Entry(middle_frame, relief="solid", borderwidth=1, background="white", width=3, textvariable=new_sale_amount_var)
new_sale_amount.pack(side="left", ipadx=10, padx=10, pady=3)

new_sale_button = Button(middle_frame, text="Add", command=lambda: add_sale(new_sale_name_var.get(), new_sale_amount_var.get(), sales_data))
new_sale_button.pack(side="right", ipadx=10, padx=10, pady=3)


#Item Addition:

bottom_frame = Frame(root)
bottom_frame.pack(padx=50, pady=10)

new_item_label = Label(bottom_frame, text="Add Item:", font = "Helvetica 12 bold italic")
new_item_label.pack(side="left", ipadx=10, padx=10, pady=3)

new_item_var = StringVar() 
new_item_var.set("Item Name")
new_item = Entry(bottom_frame, relief="solid", borderwidth=1, background="white", width=10, textvariable=new_item_var)
new_item.pack(side="left", ipadx=10, padx=10, pady=3)

new_item_profit_var = StringVar() 
new_item_profit_var.set("Profit")
new_item_profit = Entry(bottom_frame, relief="solid", borderwidth=1, background="white", width=5, textvariable=new_item_profit_var)
new_item_profit.pack(side="left", ipadx=10, padx=10, pady=3)

new_item_button = Button(bottom_frame, text="Add", command=lambda: add_item(new_item_var.get(), int(new_item_profit_var.get()), sales_data))
new_item_button.pack(side="right", ipadx=10, padx=10, pady=3)


#Total Profit

total_profit_label = Label(root, font = "Helvetica 12 bold italic", text=f"Total Profit: {total_profit} €")
total_profit_label.pack(pady=15)

root.mainloop()