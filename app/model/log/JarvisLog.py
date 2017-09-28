import logging


class JarvisLog:

    @classmethod
    def configure_log(cls):
        """logging.basicConfig(
            filename='../log/jarvisApp.log',
            level=logging.DEBUG,
            format='%(relativeCreated)6d %(threadName)s %(message)s')"""
        logging.basicConfig(level=logging.DEBUG, format='%(relativeCreated)6d %(threadName)s %(message)s')
