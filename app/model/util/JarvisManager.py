from model.comunication.MessageServer import MessageServer
from model.worker.ProcessHandler import ProcessHandler


class JarvisManager:
    jarvis = None
    message_server = None
    message_client = None
    process_handler = None

    @classmethod
    def create_threads(cls):
        cls.message_server = MessageServer()
        cls.process_handler = ProcessHandler()
        pass

    @classmethod
    def start_threads(cls):
        JarvisManager.message_server.start()
        JarvisManager.process_handler.start()
        pass

    @classmethod
    def stop_threads(cls):
        JarvisManager.message_server.stop()
        JarvisManager.process_handler.stop()
        pass

    @classmethod
    def wait_joins(cls):
        JarvisManager.message_server.join()
        JarvisManager.process_handler.join()
        pass

    @classmethod
    def add_to_process_queue(cls, message_str):
        cls.process_handler.add_to_queue(message_str)
        pass

    @classmethod
    def send_message(cls, message):
        cls.message_server.send_message(message)
