from datetime import datetime
from ghTools.logger import Logger
from ghTools.model import _Model


class Climate:
    'Represent data from sensor with temp and humi'

    def __init__(self, sensor=..., temperature=100, humidity=...):
        self.sensor = sensor
        self.date = datetime.now()
        self.temp = temperature
        self.humi = humidity
        self.logger = Logger().get_logger()
        self.model = _Model()

    def get_last_items(self, days):
        message = {
            'request': 'get_last_items',
            'data': {
                'sensor': self.sensor,
                'days': days
            }
        }

    def insert_climate(self):
        self.model.insert_climate(sensor=self.sensor, date=self.date,
                                  tempe=self.temp, humi=self.humi)

    def serialize(self):
        data_sensor = {
            'sensor': self.sensor,
            'data': {
                'temp': self.temp,
                'humi': self.humi,
                'date': self.date
            }
        }
        # return json.dumps(data_sensor)
        return (data_sensor)

    def deserialize(self, data_sensor):
        data_sensor = dict(data_sensor)
        self.sensor = data_sensor['sensor']
        self.temp = data_sensor['data']['temp']
        self.humi = data_sensor['data']['humi']
        self.date = data_sensor['data']['date']

    def print(self):
        print('sensor:{} date:{} temp:{} humi:{}'
              .format(self.sensor, self.date, self.temp, self.humi))
