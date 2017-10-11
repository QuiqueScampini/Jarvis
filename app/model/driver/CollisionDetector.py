import logging
from threading import Thread


class CollisionDetector(Thread):

    can_go_forward = True
    can_go_backward = True

    def __init__(self):
        Thread.__init__(self)
        self.setName('CollisionDetector')
        self.active = True

    def run(self):
        while self.active:
            logging.info('Detecting collisions and shit')
            self.active = False
        pass
