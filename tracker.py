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

        # top label
        self.label = ttk.Label(self.root, text="Daily Employees Page", padding=10)
        self.label.pack()  

        # scroller stuff
        self.scroller = Scrollbar(self.root, orient='horizontal') 
        self.scroller.pack(side=BOTTOM,fill='x')

        # text 
        self.text = Text(self.root, font=("Calibri, 16"), wrap=NONE, xscrollcommand=self.scroller.set)
        self.text.pack() 

        # add from file here 
        self.saveFile = open("savefile.txt", "r")
        
        for line in self.saveFile.readlines():
            self.text.insert(END, line)    

        self.saveFile.close()

        # attach scroller
        self.scroller.config(command=self.text.xview)



        # mainloop
        self.root.mainloop()

    def update(self):
        print ('update the saved file here') 

# project runs here
gui()
