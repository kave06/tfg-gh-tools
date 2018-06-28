from greenhouse.relay import Relay

class Irrigation():

    def __init__(self, relay, start=0, duration=0):
        self.relay = Relay()
        self.start = start
        self.duration = duration