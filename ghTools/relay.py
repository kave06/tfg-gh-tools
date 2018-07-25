import configparser
from os import path

import paho.mqtt.publish as publish

from ghTools.logger import Logger

APP_PATH = path.abspath(__name__)
APP_PATH = path.split(APP_PATH)
PATH_CONF = path.join(APP_PATH[0], 'etc/config.ini')

config = configparser.ConfigParser()
config.read(PATH_CONF)


class Relay:

    def __init__(self, id, state='OFF'):
        self.id = id
        self.state = state
        self.logger = Logger().get_logger()

    def set_state(self, state):
        self.state = state

        publish.single(config.get('mqtt', 'topic_relay') + '{}'.format(self.id),
                       payload=self.state, hostname=config.get('mqtt', 'host'),
                       port=config.getint('mqtt', 'port'),
                       auth={'username': config.get('mqtt', 'user'),
                             'password': config.get('mqtt', 'passw')})

        self.logger.debug(config.get('mqtt', 'host') + '{} payload:{} hostname:{} port:{}'
                          .format(self.id, self.state, config.get('mqtt', 'host'),
                                  config.getint('mqtt', 'port')))
