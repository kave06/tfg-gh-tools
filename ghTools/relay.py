import paho.mqtt.publish as publish
from time import sleep

from ghTools.config import broker_host, broker_port
from ghTools.logger import Logger

class Relay:

    def __init__(self, id, state='OFF'):
        self.id = id
        self.state = state
        self.logger = Logger().get_logger()

    def set_state(self, state):
        self.state = state
        publish.single('greenhouse/relay{}'.format(self.id), payload=self.state,
                       hostname=broker_host, port=broker_port)
        self.logger.debug('greenhouse/relay{} payload:{} hostname:{} port:{}'.format(self.id, self.state,
                       broker_host, broker_port))


if __name__ == '__main__':
    relay = Relay(id=4, state='ON')
    relay.set_state('ON')
    sleep(2)
    # relay.state = 'OFF'
    relay.set_state('OFF')
