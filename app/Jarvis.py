from model.comunication import MessageServer, MessageClient
from model.util import JarvisManager
from model.worker import ProcessHandler
import model.log.JarvisLog
import logging


class Jarvis:

    def __init__(self):
        JarvisManager.message_server = MessageServer.MessageServer(1)
        JarvisManager.process_handler = ProcessHandler.ProcessHandler(2)
        JarvisManager.message_client = MessageClient.MessageClient(3)

    def start(self):
        model.log.JarvisLog.configure_log()
        logging.info('Starting Jarvis')
        JarvisManager.message_server.start()
        JarvisManager.process_handler.start()
        #JarvisManager.message_client.start()
        logging.debug('start GPS Tracker')

    def stop(self):
        logging.debug('Stopping server')
        JarvisManager.message_server.stop()
        JarvisManager.process_handler.stop()

    def wait_joins(self):
        JarvisManager.message_server.join()
        JarvisManager.process_handler.join()
        pass

if __name__ == '__main__':
    jarvisInstance = Jarvis()
    JarvisManager.jarvis = jarvisInstance
    jarvisInstance.start()
    JarvisManager.process_handler.process_message("{\"messageType\":\"6\",\"side\":\"9\"}")
    jarvisInstance.wait_joins()
    logging.debug('End')
