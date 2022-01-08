from ping3 import ping
import time
from threading import Thread


class ping_logger:
    ip_to_ping = "8.8.8.8"
    max_ping_results = 100
    max_ping_axis = 100
    ping_results = []  # Stores our last ping values, up to max_ping_results
    started = False
    delay = 0.05  # Seconds
    timeout = 1  # Seconds
    verbose = False

    def __init__(self):
        self.ping_thread = Thread(target=self.get_ping, name="Ping Thread")

    def get_ping(self):
        self.log("Attempting to get ping. Started = "+str(self.started))
        while self.started:
            self.log("Getting ping")
            if len(self.ping_results) >= self.max_ping_results:
                self.ping_results.pop(0)
            result = ping(self.ip_to_ping, timeout=self.timeout)
            if result is None:
                result = 0
            self.log("Ping was: "+str(result))
            self.ping_results.append(result*1000)
            time.sleep(self.delay)

    def start_pinging(self):
        self.log("Starting ping")
        self.started = True
        self.ping_thread.start()

    def stop_pinging(self):
        self.log("Ending ping")
        self.started = False
        self.ping_thread.join()

    def log(self, str):
        if self.verbose:
            print(str)
