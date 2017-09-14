from model.comunication import MessageServer
from model.loggin import JarvisLog
import time
import logging


class Jarvis:
    message_receptor = MessageServer.MessageServer(1)

    def start(self):
        JarvisLog.JarvisLog().configure_log()
        logging.debug('Starting server')
        self.message_receptor.start()
        logging.debug('Start handler messages')
        logging.debug('start GPS Tracker')

    def stop(self):
        logging.debug('Stopping server')
        self.message_receptor.stop()
        self.message_receptor.join()


if __name__ == '__main__':
    jarvisInstance = Jarvis()
    jarvisInstance.start()
    logging.debug('Waiting 4 seconds')
    time.sleep(4)
    jarvisInstance.stop()
    logging.debug('End')
