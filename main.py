import numpy as np
from ping3 import ping
import time
from matplotlib import pyplot as mp


class ping_plotter:
    ip_to_ping = "8.8.8.8"
    max_ping_results = 100
    max_ping_axis = 100
    ping_results = []
    looping = True
    last_call = 0
    delay = 0.05
    background_color = 'black'
    foreground_color = 'green'

    def __init__(self):
        fig = self.init_graph()
        while self.looping:
            if (self.last_call == 0) | (self.last_call + self.delay <= time.time()):
                self.last_call = time.time()
                self.get_ping()
                self.draw_graph(fig)

    def get_ping(self):
        if len(self.ping_results) >= self.max_ping_results:
            self.ping_results.pop(0)
        result = ping(self.ip_to_ping, timeout = 1)
        if result is None:
            result = 0
        self.ping_results.append(result*1000)
        print(self.ping_results)

    def init_graph(self):
        mp.ion()
        mp.rcParams.update({
            'toolbar' : 'None',
            'text.color': self.foreground_color,
            'axes.labelcolor':self.foreground_color,
            'axes.edgecolor':self.foreground_color,
            'ytick.color':self.foreground_color
        })
        fig = mp.figure()
        return fig

    def draw_graph(self, fig):
        mp.clf()
        mp.plot(self.ping_results)
        mp.ylabel('Ping (ms)')
        ax = mp.gca()
        ax.set_ylim(0,self.max_ping_axis)

        #Colouring
        ax.set_facecolor(self.background_color)
        fig.patch.set_facecolor(self.background_color)


        fig.canvas.draw()
        fig.canvas.flush_events()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ping_plotter()

# Idea: Ping Chart
# Have a loop ping google's DNS (8.8.8.8) every X seconds and log it to an array.
# We can then use matplotlib to display these in a graph

