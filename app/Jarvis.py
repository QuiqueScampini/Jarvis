import logging
from model.log.JarvisLog import JarvisLog
from model.comunication.MessageServer import MessageServer
from model.worker.ProcessHandler import ProcessHandler
from model.driver.CollisionDetector import CollisionDetector
from model.util.JarvisManager import JarvisManager


class Jarvis:

    def __init__(self):
        JarvisManager.message_server = MessageServer()
        JarvisManager.process_handler = ProcessHandler()
        JarvisManager.collision_detector = CollisionDetector()

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
    jarvisInstance.wait_joins()
    logging.debug('End')

