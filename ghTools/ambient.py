from datetime import datetime
from websocket import create_connection
import json


WS_IP = 'ws://127.0.0.1:8000'

class Ambient:
    'Represent data from sensor with temperature and humidity'

    def __init__(self, sensor=0, temperature=100, humidity=0):

        self.sensor = sensor
        self.date = datetime.now()
        self.temperature = temperature
        self.humidity = humidity

    def get_last_items(self, days):
        message = {
            'request' : 'get_last_items',
            'data' : {
                'sensor' : self.sensor,
                'days' : days
            }
        }
        # message = 'get_last_items,{},{}'.format(self.sensor, days)
        ws = create_connection(WS_IP)
        ws.send(json.dumps(message))
        result = ws.recv()

        for row in result:
            row.print()


    def print(self):
        print('sensor:{} {} temperature:{} humidity:{}'
              .format(self.sensor, self.date, self.temperature, self.humidity))
