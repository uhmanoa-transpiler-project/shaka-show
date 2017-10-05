import zmq
import time
import sys
import random
from  multiprocessing import Process

from zmq.eventloop import ioloop, zmqstream
ioloop.install()


def getcommand(msg):
    command = msg[0].decode('UTF-8')
    print("Received control command: %s" % command)
    if command == "Exit":
        print("Received exit command, client will stop receiving messages")
        should_continue = False
        ioloop.IOLoop.instance().stop()


def process_message(msg):
    print("Processing ... %s" % msg)


port_sub = "5558"
context = zmq.Context()
socket_sub = context.socket(zmq.SUB)
socket_sub.connect("tcp://localhost:%s" % port_sub)
socket_sub.setsockopt_string(zmq.SUBSCRIBE, "")
stream_sub = zmqstream.ZMQStream(socket_sub)
stream_sub.on_recv(getcommand)
print("Connected to publisher with port %s" % port_sub)
ioloop.IOLoop.instance().start()
print("Worker has stopped processing messages.")

