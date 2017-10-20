import zmq
import time
import sys
import random
from  multiprocessing import Process

from zmq.eventloop import ioloop, zmqstream
ioloop.install()

port = "5560"
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:%s" % port)
publisher_id = random.randrange(0,9999)
print("Running server on port: ", port)

#Publisher will take in string inputs until 'Quit' is entered.
messagedata = 0
time.sleep(.3)
while (messagedata != 150):
    messagedata += 1
    if (messagedata % 3 == 0):
        print("Fizz")
        socket.send_string("Fizz")

    if(messagedata % 5 == 0):
        print("Buzz")
        socket.send_string("Buzz")

    time.sleep(.3)
