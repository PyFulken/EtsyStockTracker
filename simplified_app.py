import tkinter
import json_handler
from tkinter import *
from tkinter import ttk

#First Data Load
stock_data = json_handler.load_data()

#Button Commands
def stock_add(new_value, old_data, key):
    print(new_value)
    if new_value == "":
        status_label.config(text="Please enter a number")
    elif new_value < 1:
        status_label.config(text="Please enter a positive number")
    elif key not in old_data:
        old_data[key] = int(new_value)
        json_handler.change_data(old_data)
        status_label.config(text="Added the new {} item".format(key))
    else:
        old_data[key] += int(new_value)
        json_handler.change_data(old_data)
        status_label.config(text="Added {} units to {}".format(new_value, key))

def stock_remove(new_value, old_data, key):
    if new_value == "":
        status_label.config(text="Please enter a number")
    else:
        old_data[key] -= int(new_value)
        json_handler.change_data(old_data)
        status_label.config(text="Removed {} units from {}".format(new_value, key))

def remove_item(old_data, key):
    if key == "":
        status_label.config(text="Please enter a name")
    elif key not in old_data:
        status_label.config(text="The item {} does not exist".format(key))
    else:
        del old_data[key]
        json_handler.change_data(old_data)
        status_label.config(text="Removed the {} item".format(key))

def populate_window(stock_data):
    row_manager = 0
    entry_box_variables = {}

    for key, value in stock_data.items():
        entry_box_variables[row_manager] = StringVar()
        stock_label = Label(stock_frame, relief="solid", borderwidth=1, background="white", width=20, height=1, anchor="w")
        stock_label.config(text=key)
        stock_label.grid(row=row_manager, column=0, ipadx=10, padx=10, pady=3)
        stock_amount = Label(stock_frame, relief="solid", borderwidth=1, background="white", width=6, height=1, anchor="e")
        stock_amount.config(text=value)
        stock_amount.grid(row=row_manager, column=1, ipadx=10, padx=10, pady=3)
        amount_label= Entry(stock_frame, relief="solid", borderwidth=1, background="white", width=6, textvariable=entry_box_variables[row_manager])
        amount_label.grid(row=row_manager, column=2, ipadx=10, padx=10, pady=3)

        add_button = Button(stock_frame, text="Add", command=lambda current_variable=row_manager, current_key=key: stock_add(entry_box_variables[current_variable].get(), stock_data, current_key))
        add_button.grid(row=row_manager, column=3, ipadx=10, padx=10, pady=3)

        remove_button = Button(stock_frame, text="Remove", command=lambda current_variable=row_manager, current_key=key: stock_remove(entry_box_variables[current_variable].get(), stock_data, current_key))
        remove_button.grid(row=row_manager, column=4, ipadx=10, padx=10, pady=3)

        row_manager += 1




#GUI
root = Tk()

#Root Window Management

root.title("EZ Stock Tracker 3000-ninator")
root.maxsize(height=root.winfo_screenheight() - 100)
root.resizable(width="False", height="False")
title_label = Label(root, text="Stock Tracker", font = "Helvetica 16 bold italic")
title_label.pack(side="top")


#Current Stock
stock_frame = Frame(root)
stock_frame.pack()

populate_window(stock_data)

#Add New Item / Remove Item
item_management_frame = Frame(root)
item_management_frame.pack(side="left", padx=7)

item_management_label = Label(item_management_frame, text="Add New Item / Remove Item", font = "Helvetica 10 bold italic", anchor="e")
item_management_label.grid(row=0, column=0, columnspan=5)

item_management_name_label = Label(item_management_frame, text="Name", font = "Helvetica 8 bold italic", anchor="e")
item_management_name_label.grid(row=1, column=0, padx=1)

item_management_name_variable = StringVar()
item_management_name_entry = Entry(item_management_frame, relief="solid", borderwidth=1, background="white", width=20, textvariable=item_management_name_variable)
item_management_name_entry.grid(row=2, column=0, padx=1)

item_management_amount_label = Label(item_management_frame, text="Amount", font = "Helvetica 8 bold italic", anchor="e")
item_management_amount_label.grid(row=1, column=1, padx=1)

item_management_amount_variable = StringVar()
item_management_amount_entry = Entry(item_management_frame, relief="solid", borderwidth=1, background="white", width=7, textvariable=item_management_amount_variable)
item_management_amount_entry.grid(row=2, column=1, padx=1)

item_management_add_button = Button(item_management_frame, text="Add New", command=lambda item=item_management_name_variable, amount=item_management_amount_variable: stock_add(int(amount.get()), stock_data, item.get()))
item_management_add_button.grid(row=2, column=2, padx=1)

item_management_remove_button = Button(item_management_frame, text="Remove Item", command=lambda item=item_management_name_entry: remove_item(stock_data, item.get()))
item_management_remove_button.grid(row=2, column=3, padx=1)


#Status Bar

status_label = Label(root, text="Waiting...", font = "Helvetica 10 bold italic")
status_label.pack(side="bottom")
refresh_button = Button(root, text="Refresh")
refresh_button.pack(side="bottom", padx=60, pady=20)
root.mainloop()