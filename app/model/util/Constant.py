import socket
"""Constants definition for all System"""


class Constant:
    MessageServerIP = socket.gethostbyname(socket.gethostname())
    #MessageServerIP = '192.168.0.10'
    MessageServerPort = 5555
    MessageServerBufferSize = 1024
    MessageServerSocketTimeOut = 3.0
