from pymysql import connect, MySQLError

from ghTools.config import *
from ghTools.ambient import Ambient
from ghTools.irrigation import Irrigation
from ghTools.logger import Logger


class Model:

    def __init__(self, sensor, host=mysql_host, port=mysql_port, user=mysql_user,
                 password=mysql_pass, db=mysql_db_name):
        self.host = host
        self.port = port
        self.user = user
        self.passw = password
        self.db = db
        self.sensor = sensor
        self.logger = Logger().get_logger()

        try:
            self.cnx = connect(host=self.host, port=self.port, user=self.user,
                               password=self.passw, db=self.db)
            self.cursor = self.cnx.cursor()
            self.logger.debug('connected to database')
        except MySQLError as err:
            self.logger.error(err)

    def insert(self, query: str):
        # self.logger.debug(query)
        try:
            self.cursor.execute(query)
            self.cnx.commit()
            self.logger.debug('inserted correctly in database')
        except MySQLError as err:
            self.logger.error(err)
        finally:
            self.cursor.close()
            self.cnx.close()

    def select_ambient(self, sensor, days) -> list:
        query = """
                SELECT sensor, date, temp, humi
                FROM sensor{}_per_hour
                ORDER BY date DESC 
                LIMIT {}
                """.format(sensor, 24 * days)
        result_set = []
        try:
            self.cursor.execute(query=query)
            for (sensor, date, temp, humi) in self.cursor:
                data_sensor = {
                    'sensor': sensor,
                    'data': {
                        'temp': temp,
                        'humi': humi,
                        'date': date
                    }
                }
                result_set.append(data_sensor)
        except MySQLError as err:
            self.logger.error(err)
        finally:
            self.cursor.close()
            self.cnx.close()

        self.logger.debug('select query done')
        self.logger.debug('connection closed to database')

        return result_set

    def insert_irrigation(self, irrigation: Irrigation):
        query = '''
                INSERT INTO irrigation(id_relay, start, end, liters)
                VALUES ({}, '{}', '{}', {})
                '''.format(irrigation.relay.id, irrigation.start,
                           irrigation.end, irrigation.liters)

        self.insert(query)
        # self.logger.debug(query)

    def get_last_temperature(self):
        last_temp = None
        query = '''
            SELECT temp
            FROM ambient_data
            WHERE sensor = '{}'
            ORDER BY date DESC 
            LIMIT 1
                '''.format(self.sensor)
        try:
            self.logger.debug('try')
            self.cursor.execute(query=query)
            last_temp = self.cursor.fetchone()
            self.logger.debug(last_temp)
        except MySQLError as err:
            self.logger.error(err)
        finally:
            self.cursor.close()
            self.cnx.close()
        # return last_temp[0]

    def get_last_humidity(self, sensor):
        last_humi = None
        query = '''
            SELECT humi
            FROM ambient_data
            WHERE sensor = '{}'
            ORDER BY date DESC 
            LIMIT 1
                '''.format(sensor)
        try:
            self.cursor.execute(query=query)
            last_humi = self.cursor.fetchone()
        except MySQLError as err:
            self.logger.error(err)
        finally:
            self.cursor.close()
            self.cnx.close()
        return last_humi

    def add_liter_irrigation(self):
        query = '''
                SELECT *
                FROM irrigation
                '''
        pass

# if __name__ == "__main__":
#     model = Model()
# rs = model.select_ambient(query)
# print('len of: {}'.format(len(rs)))
# for ambient in rs:
#     ambient.print()
# rs = model.select_ambient(1,1)
# print(rs)
