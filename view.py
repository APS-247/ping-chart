from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from threading import Thread
from matplotlib.figure import Figure

from ping_logger import ping_logger
from tkinter import *


class Application(Frame):
    max_register_ping = 100
    canvas = ""

    def __init__(self, master=None):
        self.PP = ping_logger()
        Frame.__init__(self, master)

        for i in range(100):
            self.PP.get_ping()

        # The figure that contains the plot
        self.fig = Figure(figsize=(5, 3),
                          dpi=100)

        # The plot itself
        self.ax = self.fig.add_subplot()
        self.update_graph()
        self.create_graph(master)

    def create_graph(self, master):
        master.title('Ping Graph')

        # The TkInter canvas to contain the matplotlib figure
        self.canvas = FigureCanvasTkAgg(self.fig, master=master)
        self.canvas.draw()

        # Places the canvas on the Tkinter window
        self.canvas.get_tk_widget().pack()

    def update_graph(self):
        self.ax.clear()
        self.ax.set_ylim(0, self.max_register_ping)
        self.ax.plot(self.PP.ping_results)

    def update_log(self, delay=-1):
        print("Updating log")
        self.update_graph()
        if delay != -1:
            print("update log was called with delay of:" + str(delay))
            self.after(delay, self.update_log(delay))