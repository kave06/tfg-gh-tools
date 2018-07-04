import paho.mqtt.publish as publish
from ghTools.config import broker_host, broker_port
from time import sleep


class Relay:

    def __init__(self, id, state='OFF'):
        self.id = id
        self.state = state

    def set_state(self, state):
        self.state = state
        publish.single('greenhouse/relay{}'.format(self.id), payload=self.state,
                       hostname=broker_host, port=broker_port)


if __name__ == '__main__':
    relay = Relay(id=4, state='ON')
    relay.set_state('ON')
    sleep(2)
    relay.state = 'OFF'
    relay.set_state('OFF')
