
class JarvisManager:
    jarvis = None
    message_server = None
    message_client = None
    process_handler = None
    collision_detector = None

    @classmethod
    def start_threads(cls):
        cls.message_server.start()
        cls.process_handler.start()
        cls.collision_detector.start()
        pass

    @classmethod
    def stop_threads(cls):
        cls.message_server.stop()
        cls.process_handler.stop()
        cls.collision_detector.stop()
        pass

    @classmethod
    def wait_joins(cls):
        cls.message_server.join()
        cls.process_handler.join()
        cls.collision_detector.join()
        pass

    @classmethod
    def add_to_process_queue(cls, message_str):
        cls.process_handler.add_to_queue(message_str)
        pass

    @classmethod
    def send_message(cls, message):
        cls.message_server.send_message(message)
