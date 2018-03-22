from ipaddress import *
from random import randint

class IPv4RandomNetwork(IPv4Network):
    def __init__(self):
        IPv4Network.__init__(self,
                                       (randint(0x0B000000, (0xDF000000)
), randint(8, 24)), strict=False)




n = IPv4RandomNetwork()
g=list(n)
print(n)