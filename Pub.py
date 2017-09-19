#Publisher: Sends out message every few seconds

import zmq
import sys
import time

#Create port number for publisher
port = "8888"
if len(sys.argv) > 1:
    port = sys.argv[1]
    int(port)

#Create socket as Publisher
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:%s" % port)

#Continuously send out a message every 5 seconds
while True:
    print("Sending Message")
    #message = "Hello World"
    #b = message.encode('utf-8')
    socket.send(b"Hello World!")
    print("Message sent")
    time.sleep(10)
