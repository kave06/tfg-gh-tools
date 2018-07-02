import datetime
import time, sched
from datetime import datetime, timedelta


from ghTools.relay import Relay
from ghTools.model import *

s = sched.scheduler(time.time, time.sleep)


class Irrigation():

    def __init__(self, id_relay, start: datetime, duration=0):
        self.relay = Relay(id_relay)
        self.start = start
        self.end = self.start + timedelta(minutes=duration)
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


    def set_irrigation(self):
        self.relay.state = 'ON'

    def add_scheduler(self):
        now = datetime.now()
        diff = (self.start - now).total_seconds()
        self.relay.state = 'ON'
        s.enter((self.start - now).total_seconds(), 0, self.set_irrigation)

        print(diff)

if __name__ == '__main__':
    ir = Irrigation(id_relay=4,
                    start= datetime.now() + timedelta(seconds=10), duration=10)
    # ir.insert_irrigation()

    ir.add_scheduler()

