from model.comunication import MessageServer
from model.worker import ProcessHandler
import model.log.JarvisLog
import time
import logging


class Jarvis:
    message_receptor = MessageServer.MessageServer(1)
    process_handler = ProcessHandler.ProcessHandler(2)

    def start(self):
        model.log.JarvisLog.configure_log()
        logging.info('Starting server')
        self.message_receptor.start()
        self.process_handler.start()
        logging.debug('start GPS Tracker')

    def stop(self):
        logging.debug('Stopping server')
        self.message_receptor.stop()
        self.process_handler.stop()
        self.message_receptor.join()
        self.process_handler.join()


if __name__ == '__main__':
    jarvisInstance = Jarvis()
    jarvisInstance.start()
    logging.debug('Waiting 4 seconds')
    time.sleep(5)
    jarvisInstance.stop()
    logging.debug('End')
