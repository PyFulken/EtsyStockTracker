import tkinter
from tkinter import *
from tkinter import ttk
import pymongo
import sys
import platform
import psutil
import requests


mongo = pymongo.MongoClient("mongodb+srv://root:Anna1Anna2Anna3@stocktracker.qgcja.mongodb.net/stock?retryWrites=true&w=majority")
prints = mongo["print"]
prints.insert_one({"name": "Peter", "address": "Lowstreet 27"})


root = Tk()

#Root Window Management
root.title("Monitoring Windows")
screen_height = root.winfo_screenheight() - 100
screen_width = root.winfo_screenwidth() - 100
root.geometry("{}x{}".format(screen_width,screen_height))
root.resizable(width="False", height="False")


disk_label = ttk.Label(root, text="Disk Monitoring", justify="center", font="arial 20 bold", wrap=350)
disk_label.pack(ipadx=20)
disk_frame = Frame(root)
disk_frame.pack()
cpu_title_label = ttk.Label(root, text="CPU Monitoring", justify="center", font="arial 20 bold", wrap=350)
cpu_title_label.pack(ipadx=20)
cpu_frame = Frame(root)
cpu_frame.pack()
cpu_label = ttk.Label(cpu_frame, justify="center", font="arial 10 bold", wrap=350)
cpu_label.pack()

root.mainloop()