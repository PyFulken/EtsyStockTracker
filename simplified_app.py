import tkinter
from tkinter import *
from tkinter import ttk


#GUI
root = Tk()

#Root Window Management

root.title("Monitoring Windows")
screen_height = 600
screen_width = 600
root.geometry("{}x{}".format(screen_width,screen_height))
root.resizable(width="False", height="False")


#Current Stock
stock_label_parent = ttk.Label(root)
stock_label_parent.pack()
stock_label = ttk.Label(stock_label_parent)
stock_label.pack()


root.mainloop()