#Constants definition for all System
import socket

class Constant:
    MessageServerIP = socket.gethostbyname(socket.gethostname())
    MessageServerPort = 5555
    MessageServerBufferSize = 1024  # Normally 1024, but we want fast response
    MessageServerSocketTimeOut = 3.0
