from pymysql import connect, MySQLError
from datetime import datetime, timedelta

from ghTools.config import *
from ghTools.ambient import Ambient
from ghTools.logger import Logger

FORMAT = '%Y-%m-%d %H:%M:%S.%f'


class _Model:

    def __init__(self, host=mysql_host, port=mysql_port, user=mysql_user,
                 password=mysql_pass, db=mysql_db_name):
        self.host = host
        self.port = port
        self.user = user
        self.passw = password
        self.db = db
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

    def select(self, query: str):
        try:
            self.cursor.execute(query=query)
            rs = self.cursor.fetchall()
            self.logger.debug(rs)
        except MySQLError as err:
            self.logger.error(err)
        finally:
            self.cursor.close()
            self.cnx.close()
        return rs

    def select_ambient(self, sensor, days) -> list:
        query = """
                SELECT sensor, date, temp, humi
                FROM sensor{}_per_hour
                ORDER BY date DESC 
                LIMIT {}
                """.format(sensor, 24 * days)
        rs = self.select(query)
        result_set = []
        # self.cursor.execute(query=query)
        for (sensor, date, temp, humi) in rs:
            data_sensor = {
                'sensor': sensor,
                'data': {
                    'temp': temp,
                    'humi': humi,
                    'date': date
                }
            }
            result_set.append(data_sensor)

        return result_set

    def insert_irrigation(self, id_relay, start: datetime, end: datetime, liters=0) -> bool:
        collision = self.__check_irrigation_collision(start=start, end=end)
        if collision:
            self.logger.info('there are irrigaition in the same hours')
        else:
            query = '''
                    INSERT INTO irrigation(id_relay, start, end, liters)
                        VALUES ({}, '{}', '{}', {})
                    '''.format(id_relay, start, end, liters)
            self.insert(query)
        # self.logger.debug(query)

        return not collision

    def __check_irrigation_collision(self, start: datetime, end: datetime) -> bool:

        query = '''
                SELECT * 
                FROM irrigation 
                WHERE id_relay={} AND NOT
                    (
                    irrigation.start > '{}' OR 
                    irrigation.end < '{}'
                    ) 
                '''.format(self.device, end, start)
        rs = self.select(query=query)
        print(rs)
        print(type(rs))
        if rs:
            return True
        else:
            return False

    def get_last_temperature(self, id):
        last_temp = None
        query = '''
            SELECT temp 
            FROM ambient_data
            WHERE sensor = '{}'
            ORDER BY date DESC 
            LIMIT 1
                '''.format(id)
        try:
            self.cursor.execute(query=query)
            last_temp = self.cursor.fetchone()
            self.logger.debug(last_temp)
        except MySQLError as err:
            self.logger.error(err)
        finally:
            self.cursor.close()
            self.cnx.close()
        return last_temp[0]

    def get_last_humidity(self, id):
        last_humi = None
        query = '''
            SELECT humi
            FROM ambient_data
            WHERE sensor = '{}'
            ORDER BY date DESC 
            LIMIT 1
                '''.format(id)
        try:
            self.cursor.execute(query=query)
            last_humi = self.cursor.fetchone()
        except MySQLError as err:
            self.logger.error(err)
        finally:
            self.cursor.close()
            self.cnx.close()
        return last_humi[0]

    def add_liter_irrigation(self):
        query = '''
                SELECT *
                FROM irrigation
                '''
        pass


if __name__ == "__main__":
    model = Model(4)
    start = datetime.now()
    end = start + timedelta(hours=1)
    collision_start1 = datetime(2018, 7, 18, 20, 25, 0)
    collision_end1 = datetime(2018, 7, 18, 20, 30, 0)
    collision_start2 = datetime(2018, 7, 18, 20, 27, 0)
    collision_end2 = datetime(2018, 7, 18, 20, 30, 0)
    collision_start3 = datetime(2018, 7, 18, 21, 2, 0)
    collision_end3 = datetime(2018, 7, 18, 21, 35, 0)
    # model.check_irrigation(start=collision_start1, end=collision_end1)
    # condition = model.check_irrigation(start=collision_start3, end=collision_end3)
# rs = model.select_ambient(query)
# print('len of: {}'.format(len(rs)))
# for ambient in rs:
#     ambient.print()
# rs = model.select_ambient(1,1)
# print(rs)
