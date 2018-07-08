import logging

class Logger:

    # def create_log(file: str) -> logging:
    @staticmethod
    def create_log() -> logging:
        # historic = file + '_historic.log'
        file = './log/' + 'logger.log'
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        fh = logging.FileHandler(file, mode='w')
        # fh_historic = logging.FileHandler(historic, mode='a')
        fh.setLevel(logging.DEBUG)
        # fh_historic.setLevel(logging.ERROR)
        ch = logging.StreamHandler()
        ch.setLevel(logging.ERROR)
        logger.findCaller()
        formatter = logging.Formatter('%(asctime)s  %(levelname)-8s %(filename)-14s %(funcName)-15s:%(lineno)-3s  '
                                      '%(message)s')
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)
        # fh_historic.setFormatter(formatter)
        logger.addHandler(fh)
        # logger.addHandler(fh_historic)
        return logger
