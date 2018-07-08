from pymysql import connect, MySQLError
# from .config import *
from ghTools.config import *
from ghTools.ambient import Ambient
from ghTools.irrigation import Irrigation


class Model:

    def __init__(self):
        try:
            self.cnx = connect(host=mysql_host, port=mysql_port,
                               user=mysql_user, password=mysql_pass,
                               db=mysql_db_name)
            self.cursor = self.cnx.cursor()
        except MySQLError as err:
            print(err)

    def insert(self, query: str):
        self.cursor.execute(query)
        self.cnx.commit()
        # cursor.close()
        # self.cnx.close()

    def select_ambient(self, sensor, days):
        query = """
                SELECT sensor, date, temp, humi
                FROM sensor{}_per_hour
                ORDER BY date DESC 
                LIMIT {}
                """.format(sensor, 24 * days)
        result_set = []
        self.cursor.execute(query=query)
        for (sensor, date, temp, humi) in self.cursor:
            # ambient = Ambient()
            data_sensor = {
                'sensor': sensor,
                'data': {
                    'temp': temp,
                    'humi': humi,
                    'data': date
                }
            }
            # ambient.sensor = sensor
            # ambient.date = date
            # ambient.temperature = temp
            # ambient.humidity = humi
            result_set.append(data_sensor)

        self.cursor.close()
        self.cnx.close()

        return result_set

    def insert_irrigation(self, irrigation: Irrigation):
        query = '''
                INSERT INTO irrigation(id_relay, start, end, liters)
                VALUES ({}, '{}', '{}', {})
                '''.format(irrigation.relay.id, irrigation.start,
                           irrigation.end, irrigation.liters)

        self.insert(query)

    def add_liter_irrigation(self):
        query = '''
                SELECT *
                FROM irrigation
                '''
        pass


if __name__ == "__main__":
    model = Model()
    # rs = model.select_ambient(query)
    # print('len of: {}'.format(len(rs)))
    # for ambient in rs:
    #     ambient.print()
    # rs = model.select_ambient(1,1)
    # print(rs)
