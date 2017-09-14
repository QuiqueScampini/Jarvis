from threading import Thread
import socket


class MessageClient(Thread):

    message_socket = None
    val = None
    active = False

    def __init__(self, val):
        Thread.__init__(self)
        self.val = val
        self.start_socket()
        self.active = True

    def start_socket(self):
        self.message_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.message_socket.connect(('192.168.0.81', 4444))

    def run(self):
        print("Aca arranca un thread que recibe una cola de mensajes al cliente y los envia")
        while self.active:
            print("Working sending messages")
        self.message_socket.close()

    def stop(self):
        self.active = False

    #TODO Bullshit Methods
    def send_battery_level(self, client, level):
        message = "{'messageType':'7','batteryLevel':'" + str(level) + "'}\n"
        client.send(message.encode())

    def send_obstacle_detected(self, client, side):
        message = "{'messageType':'6','side':'" + str(side) + "'}\n"
        client.send(message.encode())

    def send_error(self, client, error, stacktrace):
        message = "{'messageType':'9','stackTrace':'" + stacktrace + "','error':'" + error + "'}\n"
        client.send(message.encode())


