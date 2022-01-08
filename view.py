from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from ping_logger import ping_logger
from tkinter import *


class Application(Frame):
    canvas = ""
    background_color = 'black'
    foreground_color = 'green'
    delay = int((1 / 24) * 1000) # MS, set to 24 Frames per second

    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.PP = ping_logger()
        self.PP.start_pinging()

        # The figure that contains the plot
        self.fig = Figure(figsize=(5, 3),
                          dpi=100)

        # The plot itself
        self.ax = self.fig.add_subplot()
        self.ax.set_ylim(0, self.PP.max_ping_axis)
        self.ax.set_xlim(0, self.PP.max_ping_results)
        self.axes_artist = self.ax.plot(self.PP.ping_results)
        master.title('Ping Graph')

        # The TkInter canvas to contain the matplotlib figure
        self.canvas = FigureCanvasTkAgg(self.fig, master=master)
        self.canvas.draw()

        # Places the canvas on the Tkinter window
        self.canvas.get_tk_widget().pack()

        # Starts the update loop for actually updating the graph over time
        self.after(self.delay, self.update_graph)

    def update_graph(self):
        self.axes_arti
        self.axes_artist = self.ax.plot(self.PP.ping_results)
        self.canvas.draw()
        self.after(self.delay, self.update_graph)

    def on_closing(self):
        self.PP.stop_pinging()
        self.master.destroy()
