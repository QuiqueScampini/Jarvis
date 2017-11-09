import logging
from multiprocessing import Queue
from sensorsReading.SensorsReader import SensorsReader
from processHandler.ProcessHandler import ProcessHandler
from messageServer.MessageServer import MessageServer


class Jarvis:

    def __init__(self):
        self.configure_log()
        self.process_queue = Queue()
        """PRODUCERS"""
        self.message_server = MessageServer(self.process_queue)
        self.sensors_reader = SensorsReader(self.process_queue)
        """CONSUMER"""
        self.process_handler = ProcessHandler(self.process_queue)

        self.start()

    @staticmethod
    def configure_log():
        logging.basicConfig(
            filename='../Jarvis.log',
            level=logging.DEBUG,
            format='%(relativeCreated)6d %(threadName)s %(message)s')

    def start(self):
        logging.info('Starting Jarvis')
        logging.info('Starting SensorsReader')
        self.sensors_reader.start()

    def stop_children(self):
        logging.debug('Stopping Jarvis')
        logging.debug('Stopping SensorsReader')
        self.sensors_reader.stop()

    def wait_joins(self):
        logging.debug('Waiting Joins')
        self.sensors_reader.join()
        pass


if __name__ == '__main__':
    jarvisInstance = Jarvis()
    jarvisInstance.start()
    #jarvisInstance.stop_children()
    jarvisInstance.wait_joins()
    logging.debug('End')

