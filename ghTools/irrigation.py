import datetime
import time, sched
from datetime import datetime, timedelta
from threading import Thread

from ghTools.relay import Relay
from ghTools.model import Model
from ghTools.logger import Logger

s = sched.scheduler(time.time, time.sleep)


class Irrigation():

    def __init__(self, id_relay, start: datetime, end=None, duration=0.0, liters=0):
        self.relay = Relay(id_relay)
        self.start = start
        self.duration = duration
        self.liters = liters
        self.logger = Logger().get_logger()
        self.model = Model(device=id_relay)
        if end == None:
            self.end = self.start + timedelta(minutes=duration)
        else:
            self.end = end

    # def start_irrigation(self):
    #     self.relay.state = 'ON'
    #     self.start = start
    #     self.duration = duration

    # def insert_irrigation__(self):
    #     model = Model()
    #     model.insert_irrigation(self)

    # query = '''
    #         INSERT INTO irrigation (id_relay, start, end)
    #         VALUES ({}, '{}' ,'{}')
    #         '''.format(self.relay.id, self.start, self.end)

    # print(query)

    def set_irrigation(self, state):
        self.relay.set_state(state)
        self.logger.debug('state of relay: {}'.format(self.relay.state))

    def add_scheduler(self):
        now = datetime.now()
        start = self.start - now
        start = start.total_seconds()
        end = (self.end - now).total_seconds()

        self.logger.debug('irrigation start: {}'.format(start))
        self.logger.debug('irrigation end: {}'.format(end))
        s.enter((self.start - now).total_seconds(), 0, self.set_irrigation, argument=('ON',))
        s.enter((self.end - now).total_seconds(), 0, self.set_irrigation, argument=('OFF',))
        s.run()
        self.logger.debug('irrigation end')


if __name__ == '__main__':
    logger = Logger().init_logger()
    ir = Irrigation(id_relay=4,
                    start=datetime.now() + timedelta(seconds=10), duration=0.1)
    # ir.insert_irrigation()
    ir.set_irrigation('OFF')
    # ir.set_irrigation(state='ON')
    t = Thread(target=ir.add_scheduler)
    # t.isDaemon()
    t.start()


    # ir.add_scheduler()
