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
        self.root = Tk()
        self.frame = ttk.Frame(self.root, padding=10)
        self.title = ttk.Label(self.frame, text="Weekly Hours Page", padding=10)
        self.root.mainloop()
        

# project runs here

gui()
