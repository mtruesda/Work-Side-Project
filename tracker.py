# 
# Author: Myron Truesdale
# @@Version 05/21/22
# 

# imports
from tkinter import *
from tkinter import ttk

# build the class
class gui ():
    def __init__(self):
        # Root changes
        self.root = Tk()
        self.root.geometry = ("1400x1200")
        self.root.title("Scheduling Assistant")

        # frame stuff 
        self.label = ttk.Label(self.root, text="Daily Employees Page", padding=10)
        

        self.label.pack()
        self.root.mainloop()
        

# project runs here
gui()
