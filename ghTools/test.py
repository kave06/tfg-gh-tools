from time import sleep
import logging

from ghTools.relay import Relay
from ghTools.logger import Logger



if __name__ == '__main__':
    relay = Relay(id=4, state='ON')
    relay.set_state('ON')
    sleep(2)
    relay.state = 'OFF'
    relay.set_state('OFF')
    print(logging.getLogger())


