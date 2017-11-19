import logging
import os
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
        self.process_handler = ProcessHandler(self.process_queue, self.message_server, self)

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

    def start_driving(self):
        os.system("startFilming &")
        logging.info('Starting FILMING THIS SHIT')
        pass

    def start_stitching(self):
        # TODO Send this shit to stitch the video and inform it's Done
        pass

    def stop(self):
        logging.debug('Stopping Jarvis')
        logging.debug('Stopping SensorsReader')
        self.sensors_reader.stop()
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
    # TODO After this Shut down this hole shit
    logging.debug('End')

