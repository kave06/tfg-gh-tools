import logging


class Logger():
    def __init__(self, name: str = 'greenhouse', path: str = './log/'):
        self.name = name
        self.path = path

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

    def get_logger(self):
        return logging.getLogger(__name__)
