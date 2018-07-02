import datetime
import time

from ghTools.relay import Relay
from ghTools.model import *


class Irrigation():

    def __init__(self, id_relay, start: datetime, duration=0):
        self.relay = Relay(id_relay)
        self.start = start
        self.end = self.start + datetime.timedelta(minutes=duration)
        self.duration = duration

    def start_irrigation(self):
        self.relay.state = 'ON'
        self.start = start
        self.duration = duration

    def insert_irrigation(self):

        query = '''
                INSERT INTO irrigation (id_relay, start, end)
                VALUES ({}, '{}' ,'{}')
                '''.format(self.relay.id, self.start, self.end)

        # print(query)
        model = Model()
        model.insert(query=query)

if __name__ == '__main__':
    ir = Irrigation(id_relay=4,
                    start= datetime.datetime.now(), duration=10)
    ir.insert_irrigation()
