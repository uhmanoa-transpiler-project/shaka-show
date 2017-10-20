import zmq
import time
import sys
import random
from  multiprocessing import Process

from zmq.eventloop import ioloop, zmqstream
ioloop.install()

port = "5558"
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:%s" % port)
publisher_id = random.randrange(0,9999)
print("Running server on port: ", port)

#Publisher will take in string inputs until 'Quit' is entered.
messagedata = 0
time.sleep(0.5)
while (messagedata != 100):
    messagedata += 1
    print("%s" % (messagedata))
    socket.send_string("%s" % (messagedata))
    time.sleep(0.5)
