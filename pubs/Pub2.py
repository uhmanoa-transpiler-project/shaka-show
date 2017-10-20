import zmq
import time
import sys
import random
from  multiprocessing import Process

from zmq.eventloop import ioloop, zmqstream
ioloop.install()

port = "5559"
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:%s" % port)
publisher_id = random.randrange(0,9999)
print("Running server on port: ", port)

#Publisher will take in string inputs until 'Quit' is entered.
messagedata = 0
time.sleep(1)
while (messagedata != 50):
    messagedata += 1
    print("Hello!!!!!!!!!!!!!!!!!!!!!!!")
    socket.send_string("Hello!!!!!!!!!!!!!!!!!!!!!!!")
    time.sleep(1)
