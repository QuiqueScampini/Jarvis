import os
import csv

from domain.Point import Point
from ultron.Ultron import Ultron


class UltronDemoTester:

    roads_path = "./Roads/"
    result_path = "./Results/"

    def __init__(self):
        self.files_list = None
        pass

    def process_files(self):
        for file_name in self.get_files_list():
            ultron_tester.process_file(file_name)

    def get_files_list(self):
        self.files_list = []
        for file_name in os.listdir(self.roads_path):
            if file_name.endswith(".csv"):
                self.files_list.append(file_name)
        return self.files_list

    def process_file(self, file_name):
        ultron = Ultron(None)
        ultron.optimize_road(self.get_points_from_file(file_name))
        ultron.generate_steps()
        self.dump_ultron(ultron, file_name)
        pass

    def get_points_from_file(self, file_name):
        file_point_list = []
        file_path = self.roads_path + file_name
        with open(file_path, newline='') as road_file:
            spam_reader = csv.reader(road_file, delimiter=',')
            # Ignore first line (Header)
            spam_reader.__next__()
            number = 0
            for row in spam_reader:
                if row:
                    file_point_list.append(Point(len(file_point_list), float(row[0]), float(row[1]), float(row[2])))
                    number += 1
            return file_point_list

    def dump_ultron(self, ultron, file_name):

        only_file_name, file_extension = os.path.splitext(file_name)
        optimized_file_path = self.result_path + only_file_name + "_optimized" + file_extension
        steps_file_path = self.result_path +  only_file_name + "_steps" + file_extension

        self.dump_optimized_road(ultron.optimized_road, optimized_file_path)
        self.dump_steps(ultron.steps, steps_file_path)
        pass

    @staticmethod
    def dump_optimized_road(optimized_road, optimized_file_path):
        spam_writer = csv.writer(open(optimized_file_path, "w", newline=''), delimiter=",")
        spam_writer.writerow(["Latitude", "Longitude", "Elevation"])
        for point in optimized_road:
            spam_writer.writerow([point.latitude, point.longitude, point.elevation])
        pass

    @staticmethod
    def dump_steps(steps, steps_file_path):
        spam_writer = csv.writer(open(steps_file_path, "w", newline=''), delimiter=",")
        spam_writer.writerow(["Rotation Direction", "Rotation Angle", "Time Forward [s]"])
        for step in steps:
            spam_writer.writerow([step.direction.name, "%.2f" % step.angle, "%.2f" % step.seconds])
        pass


if __name__ == '__main__':
    ultron_tester = UltronDemoTester()
    ultron_tester.process_files()
