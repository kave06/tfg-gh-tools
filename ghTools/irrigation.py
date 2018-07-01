import datetime
import time
from ghTools.relay import Relay


class Irrigation():

    def __init__(self, relay_id, start=0, duration=0):
        self.relay = Relay(relay_id)
        self.start = start
        self.duration = duration


    def start_irrigation(self, start:datetime, duration:time):
        self.relay.state = 'ON'
        self.start = start
        self.duration = duration
