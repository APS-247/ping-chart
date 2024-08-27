from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from ping_logger import ping_logger
from tkinter import *


class Application(Frame):
    canvas = ""
    background_color = 'black'
    foreground_color = 'green'
    fps = 5 # How many times we're going to redraw the graph a second
    delay = int((1 / fps) * 1000) # MS

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
        self.ax.plot(self.PP.ping_results)
        master.title('Ping Graph')

        # The TkInter canvas to contain the matplotlib figure
        self.canvas = FigureCanvasTkAgg(self.fig, master=master)
        self.canvas.draw()

        # Places the canvas on the Tkinter window
        self.canvas.get_tk_widget().place(relx=0.5, rely=0, relheight=0.8, relwidth=1, anchor='n')

        Frame1 = Frame(self.master, bd=5, bg=self.background_color)
        Frame1.place(relx=0.5, rely=0.8, relheight=0.2, relwidth=1, anchor='n')

        self.averageping = Label(Frame1, text="Ave:"+str(self.PP.ping_average))
        self.averageping.place(relx=0, rely=0.5, relheight=0.4, relwidth=0.5)

        self.highestping = Label(Frame1, text="Max:"+str(self.PP.ping_highest))
        self.highestping.place(relx=0.55, rely=0.5, relheight=0.4, relwidth=0.5)

        # Starts the update loop for actually updating the graph over time
        self.anim = animation.FuncAnimation(self.fig, self.update_graph, interval=self.delay)

    def update_graph(self, i):
        self.ax.clear()
        self.ax.set_ylim(0, self.PP.max_ping_axis)
        self.ax.set_xlim(0, self.PP.max_ping_results)
        self.ax.set_ylabel('Ping (ms)')
        self.ax.plot(self.PP.ping_results)
        # self.ax.
        self.averageping.config(text="Ave:"+str(self.PP.ping_average))
        self.highestping.config(text="Max:"+str(self.PP.ping_highest))
        # self.canvas.draw()

    def on_closing(self):
        self.PP.stop_pinging()
        self.master.destroy()
