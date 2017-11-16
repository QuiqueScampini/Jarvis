import socket
import logging
from threading import Thread
from util.Constant import Constant


class MessageServer(Thread):

    def __init__(self, process_queue):
        Thread.__init__(self)
        self.setName('MessageServer')
        self.process_queue = process_queue
        self.active = False
        self.waiting_client = True
        # Socket Definition
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
                    logging.debug('Message received ' + message_str)
                    self.process_queue.put(message_str)
                    self.connection.send(message)
                else:
                    break
        finally:
            if self.connection:
                self.connection.close()
        logging.info('Stop server Server')

    def accept_client(self):
        logging.info('Start message Server')
        while self.waiting_client:
            try:
                self.connection, self.client_address = self.message_socket.accept()
                logging.info('Client Connected ' + self.client_address[0])
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
