import logging


class Logger():
    def __init__(self, name: str = 'greenhouse', path: str = './log/'):
        self.name = name
        self.path = path

    # @staticmethod
    def init_logger(self) -> logging:
        file_debug = self.path + self.name + '_debug.log'
        file_hist = self.path + self.name + '.log'
        formatter = logging.Formatter('%(asctime)s %(levelname)-8s %(filename)-14s '
                                      '%(funcName)-15s:%(lineno)-3s %(message)s')

        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)

        fh1 = logging.FileHandler(filename=file_debug, mode='w+')
        fh2 = logging.FileHandler(filename=file_hist, mode='a+')

        fh1.setLevel(logging.DEBUG)
        fh2.setLevel(logging.ERROR)

        fh1.setFormatter(formatter)
        fh2.setFormatter(formatter)

        logger.addHandler(fh1)
        logger.addHandler(fh2)

        return logger


    # @staticmethod
    def get_logger(self):
        return logging.getLogger(__name__)

    # def create_logger(self, name):
    #     path = './log/'
    #     file_debug = path + name + '_debug.log'
    #     file_hist = path +name + '.log'
    #     formatter = logging.Formatter('%(asctime)s %(levelname)-8s %(filename)-14s %(funcName)-15s:%(lineno)-3s  '
    #                                   '%(message)s')
    #     logger = logging.getLogger(__name__)
    #     logger.setLevel(logging.DEBUG)
    #
    #     fh1 = logging.FileHandler(filename=file_debug, mode='w+')
    #     fh2 = logging.FileHandler(filename=file_hist, mode='a+')
    #
    #     fh1.setLevel(logging.DEBUG)
    #     fh2.setLevel(logging.ERROR)
    #
    #     fh1.setFormatter(formatter)
    #     fh2.setFormatter(formatter)
    #
    #     logger.addHandler(fh1)
    #     logger.addHandler(fh2)
    #
    #
    #
    # # def create_log(file: str) -> logging:
    # @staticmethod
    # def create_log() -> logging:
    #     # historic = file + '_historic.log'
    #     file = './log/' + 'logger.log'
    #     logger = logging.getLogger(__name__)
    #     logger.setLevel(logging.DEBUG)
    #     fh = logging.FileHandler(file, mode='w+')
    #     # fh_historic = logging.FileHandler(historic, mode='a')
    #     fh.setLevel(logging.DEBUG)
    #     # fh_historic.setLevel(logging.ERROR)
    #     ch = logging.StreamHandler()
    #     ch.setLevel(logging.ERROR)
    #     logger.findCaller()
    #     formatter = logging.Formatter('%(asctime)s %(levelname)-8s %(filename)-14s %(funcName)-15s:%(lineno)-3s  '
    #                                   '%(message)s')
    #     ch.setFormatter(formatter)
    #     fh.setFormatter(formatter)
    #     # fh_historic.setFormatter(formatter)
    #     logger.addHandler(fh)
    #     # logger.addHandler(fh_historic)
    #     return logger
