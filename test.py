import tkinter
from tkinter import *
from tkinter import ttk
from MongoDB import *

import requests

#Mongo Connection
connect = connect_to_db()

add_stock(connect["prints"], "Stamps", 10)

#GUI
root = Tk()

#Root Window Management
root.title("Monitoring Windows")
screen_height = root.winfo_screenheight() - 100
screen_width = root.winfo_screenwidth() - 100
root.geometry("{}x{}".format(screen_width,screen_height))
root.resizable(width="False", height="False")

#Login page

root.mainloop()