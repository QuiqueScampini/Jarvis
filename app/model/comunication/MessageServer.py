from threading import Thread
from model.util import Constant
from model.worker import ProcessHandler
import socket
import logging


class MessageServer(Thread):

    val = None
    active = None
    waiting_client = None
    message_socket = None
    connection = None
    client_address = None

    def __init__(self, val):
        Thread.__init__(self)
        self.setName('MessageServer')
        self.val = val
        self.start_socket()
        self.active = False
        self.waiting_client = True

    def start_socket(self):
        self.message_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.message_socket.settimeout(Constant.MessageServerSocketTimeOut)
        self.message_socket.bind((Constant.MessageServerIP, Constant.MessageServerPort))
        self.message_socket.listen(1)

    def run(self):
        try:
            self.accept_client()
            while self.active:
                message = self.connection.recv(Constant.MessageServerBufferSize)
                if message:
                    ProcessHandler.ProcessHandler.process_queue.put(message)
                    logging.debug('Message received' + message)
                    self.connection.send(message)  # echo
                else:
                    break
        finally:
            if self.connection:
                self.connection.close()
        logging.info('Stop server receptor')

    def accept_client(self):
        logging.info('Start message receptor')
        while self.waiting_client:
            try:
                self.connection, self.client_address = self.message_socket.accept()
                logging.info('Client Connected' + self.client_address)
                self.active = True
                self.waiting_client = False
                break
            except socket.timeout:
                logging.info('Timeout')
                pass

    def stop(self):
        if self.waiting_client:
            self.waiting_client = False
            logging.info('Not Active')
        else:
            self.active = False
            self.message_socket.shutdown(socket.SHUT_WR)
