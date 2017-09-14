import logging


class JarvisLog:

    def configure_log():
        logging.basicConfig(level=logging.DEBUG, format='%(relativeCreated)6d %(threadName)s %(message)s')