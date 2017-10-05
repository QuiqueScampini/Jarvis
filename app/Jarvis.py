import logging
from model.log.JarvisLog import JarvisLog
from model.util.JarvisManager import JarvisManager


class Jarvis:

    def __init__(self):
        JarvisManager.create_threads()

    def start(self):
        JarvisLog.configure_log()
        logging.info('Starting Jarvis')
        JarvisManager.start_threads()

    def stop(self):
        logging.debug('Stopping Jarvis')
        JarvisManager.stop_threads()

    def wait_joins(self):
        JarvisManager.wait_joins()
        pass

if __name__ == '__main__':
    jarvisInstance = Jarvis()
    JarvisManager.jarvis = jarvisInstance
    jarvisInstance.start()
    """JarvisManager.process_handler.process_message('{ "messageType": "1", "angle": 10, "power": 50}')"""
    jarvisInstance.wait_joins()
    logging.debug('End')

