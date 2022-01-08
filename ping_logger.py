from ping3 import ping


class ping_logger:
    ip_to_ping = "8.8.8.8"
    max_ping_results = 100
    max_ping_axis = 100
    ping_results = []
    timeout = 1 #Seconds
    background_color = 'black'
    foreground_color = 'green'

    def get_ping(self):
        print("getting ping:")
        if len(self.ping_results) >= self.max_ping_results:
            self.ping_results.pop(0)
        result = ping(self.ip_to_ping, timeout=self.timeout)
        if result is None:
            result = 0
        print("Ping was: "+str(result))
        self.ping_results.append(result*1000)

