from ping3 import ping
import time
from threading import Thread


class ping_logger:
    ip_to_ping = "8.8.8.8"
    max_ping_results = 50
    max_ping_axis = 200
    ping_results = []  # Stores our last ping values, up to max_ping_results
    ping_highest = 0
    ping_average = 0
    ping_sum = 0
    lost_packets = 0
    started = False
    delay = 0.5  # Seconds
    timeout = 1  # Seconds
    verbose = True

    def __init__(self):
        self.ping_thread = Thread(target=self.get_ping, name="Ping Thread")

    def get_ping(self):
        self.log("Attempting to get ping. Started = " + str(self.started))
        while self.started:
            self.log("Getting ping")
            if len(self.ping_results) >= self.max_ping_results:
                self.ping_sum -= self.ping_results[0]
                self.ping_results.pop(0)
            result = ping(self.ip_to_ping, timeout=self.timeout)
            if result is None:
                result = 0
            result = round(result*1000, 2)
            self.ping_sum += result
            if self.ping_highest < result:
                self.ping_highest = result
            if (result > self.timeout*1000) | (result == 0):
                self.lost_packets += 1
            self.ping_results.append(result)
            self.ping_average = round(self.ping_sum / len(self.ping_results), 2)
            self.max_ping_axis = max(200, round(self.ping_average, 10))
            self.log("Ping was: " + str(result) + ", new average:" + str(self.ping_average) + ", highest:" + str(
                self.ping_highest)+", Lost Packets:"+str(self.lost_packets))
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
