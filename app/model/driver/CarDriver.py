import logging

class CarDriver:

    @staticmethod
    def move_car(movement_json):
        logging.info(movement_json["angle"])
        logging.info(movement_json["power"])
