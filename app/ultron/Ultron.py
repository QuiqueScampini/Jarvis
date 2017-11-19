from math import sqrt, sin, atan2, cos, acos

from domain.Direction import Direction
from domain.ReturnStep import ReturnStep


class Ultron:

    def __init__(self, jarvis):
        self.jarvis = jarvis
        self.optimized_road = []
        self.steps = []
        self.earth_radio = 6372797.56086

    def return_origin(self):
        self.optimize_road(self.jarvis.gps_reader.point_list)
        self.generate_steps()
        self.execute_steps()

    def execute_steps(self):
        for step in self.steps:
            self.execute_step(step)

    def execute_step(self, step):
        # TODO execute step
        pass

    def optimize_road(self, point_list):
        original_list = point_list
        reversed_list = original_list.copy()
        reversed_list.reverse()

        next_position = None
        for point in original_list:
            if not next_position or point.number == next_position:
                for point2 in reversed_list:
                    if point.latitude == point2.latitude and point.longitude == point.longitude:
                        if point.number == point2.number:
                            self.optimized_road.append(point)
                            next_position = None
                        else:
                            self.optimized_road.append(point2)
                            next_position = point2.number + 1
                        break
        self.optimized_road.reverse()

    def generate_steps(self):
        conversion_constant = 57.2958

        last_point = None
        first_pass = True

        vector_x = None
        vector_y = None
        old_latitude = None
        old_longitude = None

        for point in self.optimized_road:
            if last_point:
                latitude1 = last_point.latitude
                longitude1 = last_point.longitude
                latitude2 = point.latitude
                longitude2 = point.longitude

                """Start Distance"""
                delta_lat = (latitude2 / conversion_constant) - (latitude1 / conversion_constant)
                delta_long = (longitude2 / conversion_constant) - (longitude1 / conversion_constant)
                vara = sin(delta_lat/2) * sin(delta_lat/2) + cos(latitude1/conversion_constant) * cos(latitude2/conversion_constant) * sin(delta_long/conversion_constant)*sin(delta_long/conversion_constant)
                varc = 2 * atan2(sqrt(vara), sqrt(1-vara))
                vard = self.earth_radio * varc
                """End Distance"""

                if first_pass:
                    self.steps.append(ReturnStep(vard, Direction.DIR_LEFT, 180))
                    first_pass = False
                else:
                    vector_w = latitude2 - latitude1
                    vector_z = longitude2 - longitude1

                    prodescalar = vector_x * vector_w + vector_y * vector_z

                    long_vector1 = sqrt(vector_x * vector_x + vector_y * vector_y)

                    long_vector2 = sqrt(vector_w * vector_w + vector_z * vector_z)

                    cos_tita = acos(prodescalar / (long_vector1 * long_vector2)) * conversion_constant
                    vectorcompx = latitude2 - old_latitude
                    vectorcompy = longitude2 - old_longitude
                    prodvectorial = vector_x * vectorcompy - vector_y * vectorcompx

                    direction = Direction.DIR_LEFT
                    angle = cos_tita
                    if prodvectorial > 0:
                        direction = Direction.DIR_RIGHT
                    elif prodvectorial == 0:
                        angle = 0
                    self.steps.append(ReturnStep(vard, direction, angle))
                    pass

                vector_x = latitude2 - latitude1
                vector_y = longitude2 - longitude1
                old_latitude = latitude1
                old_longitude = longitude1
                pass
            last_point = point
        pass
