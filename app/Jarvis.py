import logging
import os
import multiprocessing as multiprocess
import queue as normal_queue
from gps.GpsReader import GpsReader
from sensorsReading.SensorsReader import SensorsReader
from processHandler.ProcessHandler import ProcessHandler
from messageServer.MessageServer import MessageServer
from sensorsReading.SensorsReaderUpdater import SensorsReaderUpdater
from ultron.Ultron import Ultron


class Jarvis:

    def __init__(self):
        self.configure_log()
        self.process_queue = normal_queue.PriorityQueue()
        self.sensors_reader_queue = multiprocess.Queue()
        "Ultron"
        self.ultron = Ultron(self)
        """PRODUCERS"""
        self.message_server = MessageServer(self.process_queue, self)
        self.sensors_reader = SensorsReader(self.sensors_reader_queue)
        self.sensors_reader_updater = SensorsReaderUpdater(self.sensors_reader_queue, self.process_queue)
        """CONSUMER"""
        self.process_handler = ProcessHandler(self.process_queue, self.message_server, self.ultron, self)
        "GPS Reader"
        self.gps_reader = GpsReader(self.message_server)

    @staticmethod
    def configure_log():
        logging.basicConfig(
            filename='../Jarvis.log',
            level=logging.DEBUG,
            format='%(relativeCreated)6d %(threadName)s %(message)s')

    def start(self):
        logging.info('Starting Jarvis')
        logging.info('Starting MessageServer')
        self.message_server.start()
        logging.info('Starting ProcessHandler')
        self.process_handler.start()
        logging.info('Starting SensorsReader')
        self.sensors_reader.start()
        logging.info('Starting SensorsReader Updater')
        self.sensors_reader_updater.start()

    @staticmethod
    def start_filming():
        logging.info('Start FILMING')
        os.system("filmDrive.sh &")

    @staticmethod
    def stop_filming():
        logging.info('Starting Stitching')
        os.system("stopFilming.sh &")
        pass

    def stop(self):
        logging.debug('Stopping Jarvis')
        logging.debug('Stopping SensorsReader')
        self.sensors_reader.stop()
        logging.info('Stopping Updater')
        self.sensors_reader_updater.stop()
        logging.info('Stopping MessageServer')
        self.message_server.stop()
        logging.info('Stopping ProcessHandler')
        self.process_handler.stop()

    def wait_joins(self):
        logging.debug('Waiting Joins')
        self.sensors_reader.join()
        self.message_server.join()
        self.process_handler.join()
        pass


if __name__ == '__main__':
    jarvisInstance = Jarvis()
    jarvisInstance.start()
    jarvisInstance.wait_joins()
    logging.debug('End')

