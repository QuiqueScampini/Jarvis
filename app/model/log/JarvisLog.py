import logging


def configure_log():
    """logging.basicConfig(
        filename='../log/jarvisApp.log',
        level=logging.DEBUG,
        format='%(relativeCreated)6d %(threadName)s %(message)s')"""
    logging.basicConfig(level=logging.DEBUG, format='%(relativeCreated)6d %(threadName)s %(message)s')
