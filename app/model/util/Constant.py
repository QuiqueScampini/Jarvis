import socket
"""Constants definition for all System"""


class Constant:
    MessageServerIP = socket.gethostbyname(socket.gethostname())
    #MessageServerIP = '192.168.0.10'
    MessageServerPort = 5555
    MessageServerBufferSize = 1024
    MessageServerSocketTimeOut = 3.0

    """Gpio vales for CarDriver and CollisionDetector """
    min_backward = 1100
    #max_backward = 700
    min_forward = 1600
    #max_forward = 2000
    speed_multiplier = 4
    #brake_speed = 1300
    stop_speed = 1500

    #max_left = 1100
    middle_direction = 1350
    #max_right = 1600
    turn_dif = 250
