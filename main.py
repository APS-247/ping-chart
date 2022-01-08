from tkinter import *

from view import Application

if __name__ == '__main__':
    root = Tk()
    app = Application(master=root)
    app.mainloop()

# Idea: Ping Chart
# Have a loop ping google's DNS (8.8.8.8) every X seconds and log it to an array.
# We can then use matplotlib to display these in a graph
