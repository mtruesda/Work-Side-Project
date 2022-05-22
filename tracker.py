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
        self.frm = ttk.Frame(self.root, padding=10)
        self.root.mainloop()

# project runs here

gui()
