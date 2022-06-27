# Using Python to Create a Program that Handles number of hours per week and scheduling

This program will allow the user to plan out the shifts of employees per day of the week. It's not super automated but it saves this information to a file that gets updated through the use of a       button. I plan to implement this using TKinter and having the program access the information from a local file that can be edited so that it "saves". It probably won't be as practical as using a google sheet or an excel sheet,but it will be fun practice.

The goal is to also have a page where you can write and store the number of hours per week per employee and possibly even have the "software" do a little math totalling.

@Version 05/21/22
Project can create a tkinter window.

@Version 06/27/22
Project creates the window with a label and a horizontally scrolling text box that can be exited. The project also spawns the textbox with the contents of a savefile called savefile.txt. The number ofhours information is stored in a file called hours.txt. When you click the swap pages button you can now swap between the hours page and the scheduling page. The schedule template is set up for one   week and the hours page has a few weeks written onto it. The total counter is not yet setup to automatically place but I may just throw in a calculator. Tkinter isn't incredibly supportive of         scrolling frames and so that makes scrolling through labels difficult (also would've been tedious).

Additional Thoughts: Would be cool to implement a few of these features
- freezing panes for the names on the hours page (would require doing away with the text box or making a second one that isn't a part of the scrolling one)
- A total column that totals automatically like in excel or google sheets
- Templates that fit a bit more securely and can't be edited out of the "software"
