import socket
import logging
from threading import Thread
from util.Constant import Constant


class MessageServer(Thread):

    def __init__(self, process_queue, jarvis):
        Thread.__init__(self)
        self.setName('MessageServer')
        self.jarvis = jarvis
        self.process_queue = process_queue
        self.active = True
        self.waiting_client = True
        # Socket Definition
        self.message_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.message_socket.settimeout(Constant.MessageServerSocketTimeOut)
        self.message_socket.bind((Constant.MessageServerIP, Constant.MessageServerPort))
        self.message_socket.listen(1)
        self.connection = None
        self.client_address = None

    def run(self):
        logging.info('Start message Server')
        while self.active:
            try:
                self.accept_client()
                while self.active:
                    self.receive_messages()
            except socket.timeout:
                self.waiting_client = True
                self.jarvis.stop_filming()
                logging.info('Client Socket Timeout')
            finally:
                if self.connection:
                    logging.info('Closing connection')
                    self.connection.close()
        logging.info('Stop MessageServer')

    def accept_client(self):
        logging.info('Waiting new Client')
        while self.waiting_client:
            try:
                self.connection, self.client_address = self.message_socket.accept()
                self.connection.settimeout(Constant.MessageServerClientTimeOut)
                logging.info('Client Connected ' + self.client_address[0])
                self.waiting_client = False
                break
            except socket.timeout:
                pass

    def receive_messages(self):
        logging.info('Waiting message')
        message = self.connection.recv(Constant.MessageServerBufferSize)
        if message:
            message_str = message.decode('utf-8')
            logging.debug('Message received ' + message_str)
            self.process_queue.put(message_str)
            self.connection.send(message)

    def stop(self):
        self.active = False
        if self.waiting_client:
            self.waiting_client = False
        else:
            self.message_socket.shutdown(socket.SHUT_WR)
            self.connection = None

    def send_message(self, message):
        self.connection.send(message.encode())
