from time import sleep

from ghTools.relay import Relay


if __name__ == '__main__':
    relay = Relay(id=4, state='ON')
    relay.set_state('ON')
    sleep(2)
    relay.state = 'OFF'
    relay.set_state('OFF')
