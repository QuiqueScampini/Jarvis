from model.comunication.MessageClient import MessageClient
from model.comunication.MessageServer import MessageServer
from model.worker.ProcessHandler import ProcessHandler


class JarvisManager:
    jarvis = None
    message_server = None
    message_client = None
    process_handler = None

    @classmethod
    def create_threads(cls):
        cls.message_server = MessageServer(1)
        cls.process_handler = ProcessHandler(2)
        cls.message_client = MessageClient(3)
        pass

    @classmethod
    def start_threads(cls):
        JarvisManager.message_server.start()
        JarvisManager.process_handler.start()
        """JarvisManager.message_client.start()"""
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
