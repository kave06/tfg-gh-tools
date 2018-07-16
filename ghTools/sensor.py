# from websocket import create_connection

# WS_IP = 'ws://127.0.0.1:8000'
from ghTools import Model

class Sensor:

    def __init__(self, id: int = 0, model: str = None):
        self.id = id
        self.mod = model
        self.model = Model(self.id)

    def get_last_temperature(self):
        '''
        connect to database server and request
        :return:
        '''
        return 100

    def get_last_humidity(self):
        '''
        connect to database server and request
        :return:
        '''
        pass

    def get_last_ambient(self, days):
        message = 'get_last_items,{},{}'.format(self.id, days)
        # ws = create_connection(WS_IP)
        # ws.send(message)
        # result = ws.recv()
        #
        # for row in result:
        #     row.print()
