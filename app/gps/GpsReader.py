from threading import Thread
from time import sleep
import gpsd
from domain.Point import Point


class GpsReader(Thread):

    def __init__(self, message_server):
        Thread.__init__(self)
        self.setName('GpsReader')
        gpsd.connect()
        self.gps_reader = None
        self.point_list = []
        self.active = True
        self.message_server = message_server

    def run(self):
        self.gps_reader = gpsd.get_current()
        last_point = None
        counter = 60
        while self.active:
            point = self.get_position()
            if last_point:
                if last_point.latitude == point.longitude and last_point.longitude == point.longitude:
                    counter = counter - 1
                    if counter == 0:
                        self.inform_stuck(point)
                        counter = 60
                else:
                    counter = 60
            last_point = point

            self.point_list.append(point)
            sleep(1)

    def stop(self):
        self.active = False

    def get_position(self):
        latitude, longitude = self.gps_reader.position()
        return Point(len(self.point_list), latitude, longitude, None)

    def inform_stuck(self, point):
        # TODO send message informing we are stuck in that Point
        # self.message_server.send_message("LALALLA")
        pass
