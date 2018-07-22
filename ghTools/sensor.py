# from websocket import create_connection

from ghTools.model import _Model


class Sensor:

    def __init__(self, id: int = 0, model: str = None):
        self.id = id
        self.mod = model
        self.__model = _Model()

    def get_last_temperature(self):
        '''
        connect to database server and request
        :return:
        '''
        return self.__model.get_last_temperature(self.id)

    def get_last_humidity(self):
        '''
        connect to database server and request
        :return:
        '''
        return self.__model.get_last_humidity(self.id)

    def get_last_ambient(self, days) -> list:
        return self.__model.select_ambient(sensor=self.id, days=days)


        # message = 'get_last_items,{},{}'.format(self.id, days)
        # ws = create_connection(WS_IP)
        # ws.send(message)
        # result = ws.recv()
        #
        # for row in result:
        #     row.print()
