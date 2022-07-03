# 
# Author: Myron Truesdale
# @@Version 06/27/22
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
    
        self.setupSchedulePage()

    def updateScheduleFile(self):
        # opens the file and then writes it to the doc from the text box
        self.saveFile = open("savefile.txt","w")
        contents = self.text.get("1.0","end")
        self.saveFile.write(contents)
        self.saveFile.close()

    def updateHoursFile(self):
        self.saveFile = open("hours.txt","w")
        contents = self.hoursText.get("1.0","end")
        self.saveFile.write(contents)
        self.saveFile.close()

    def deleteItems(self):
        ## DELETION

        # pack forgets 
        self.labelTwo.pack_forget()
        self.secondScroller.pack_forget()
        self.hoursText.pack_forget()
        self.saveHours.pack_forget()
        self.swapToSchedule.pack_forget()

        self.setupSchedulePage()


    def setupSchedulePage(self):
        ## SETUP

        # top label
        self.labelOne = ttk.Label(self.root, text="Daily Employees Page", padding=10)
        self.labelOne.pack()  

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

        # attach scrollers
        self.scroller.config(command=self.text.xview)
        
        # make a save button 
        self.saveSchedule = ttk.Button(self.root, text='Save Schedule', command=self.updateScheduleFile)
        self.saveSchedule.pack()

        # swap to hours page button
        self.swapToHours = ttk.Button(self.root, text='Swap to Hours Page', command=self.setupHoursPage)
        self.swapToHours.pack()

        # mainloop
        self.root.mainloop()



    def setupHoursPage(self):
        ## DELETION

        # pack forgets
        self.labelOne.pack_forget()
        self.scroller.pack_forget()
        self.text.pack_forget()
        self.saveSchedule.pack_forget()
        self.swapToHours.pack_forget()

        ## SETUP
        
        # second top label 
        self.labelTwo = ttk.Label(self.root, text='Employee Hours Page', padding=10)
        self.labelTwo.pack()

        # scroller two stuff 
        self.secondScroller = Scrollbar(self.root, orient='vertical')
        self.secondScroller.pack(side=RIGHT,fill='y')

        # hours text 
        self.hoursText = Text(self.root, font=("Calibri, 16"), wrap=NONE,yscrollcommand=self.secondScroller.set)
        self.hoursText.pack()

        # write the text in from File 
        self.saveFile = open("hours.txt","r")
        
        for line in self.saveFile.readlines():
            self.hoursText.insert(END, line)    

        self.saveFile.close()


        # attach scroller
        self.secondScroller.config(command=self.hoursText.yview)

        # save hours button
        self.saveHours = ttk.Button(self.root, text='Save Hours', command=self.updateHoursFile)
        self.saveHours.pack()

        self.swapToSchedule = ttk.Button(self.root, text='Swap to Schedule Page', command=self.deleteItems)
        self.swapToSchedule.pack()

        # mainloop
        self.root.mainloop()

# project runs here
gui()
