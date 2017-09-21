from threading import Thread
from model.util import Constant, JarvisManager
from model.worker import ProcessHandler
import socket
import logging


class MessageServer(Thread):

    def __init__(self, val):
        Thread.__init__(self)
        self.setName('MessageServer')
        self.val = val
        self.active = False
        self.waiting_client = True
        #Socket Definition
        self.message_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.message_socket.settimeout(Constant.MessageServerSocketTimeOut)
        self.message_socket.bind((Constant.MessageServerIP, Constant.MessageServerPort))
        self.message_socket.listen(1)
        self.connection = None
        self.client_address = None

    def run(self):
        try:
            self.accept_client()
            while self.active:
                message = self.connection.recv(Constant.MessageServerBufferSize)
                message_str = message.decode('utf-8')
                if message:
                    JarvisManager.process_handler.process_queue.put(message_str)
                    logging.debug('Message received' + message_str)
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
                logging.info('Client Connected' + self.client_address[0])
                self.active = True
                self.waiting_client = False
                break
            except socket.timeout:
                pass

    def stop(self):
        if self.waiting_client:
            self.waiting_client = False
        else:
            self.active = False
            self.message_socket.shutdown(socket.SHUT_WR)

    def send_message(self, message):
        self.connection.send(message.encode())
