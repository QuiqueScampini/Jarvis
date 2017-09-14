from model.comunication import MessageServer
import time


class Jarvis:
    message_receptor = MessageServer.MessageServer(1)

    def start(self):
        self.message_receptor.start()
        print("Start handler messages")
        print("start GPS Tracker")

    def stop(self):
        self.message_receptor.stop()
        self.message_receptor.join()


if __name__ == '__main__':
    jarvisInstance = Jarvis()
    jarvisInstance.start()
    print("Waiting 4 seconds")
    time.sleep(4)
    jarvisInstance.stop()
    print("End")
