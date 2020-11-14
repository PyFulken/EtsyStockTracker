import tkinter
import json_handler
from tkinter import *
from tkinter import ttk

#First Data Load
stock_data = json_handler.load_data()

def stock_add(new_value, old_data, key):
    if new_value == "":
        status_label.config(text="Please enter a number")
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

root.title("Monitoring Windows")
root.maxsize(height=root.winfo_screenheight() - 100)
root.resizable(width="False", height="False")
title_label = Label(root, text="Stock Tracker", font = "Helvetica 16 bold italic")
title_label.pack(side="top")


#Current Stock
stock_frame = Frame(root)
stock_frame.pack()

populate_window(stock_data)


#Status Bar

status_label = Label(root, text="Waiting...", font = "Helvetica 10 bold italic")
status_label.pack(side="left")
refresh_button = Button(root, text="Refresh")
refresh_button.pack(side="right", padx=60, pady=20)
root.mainloop()