#Publisher: Sends out message every few seconds

import zmq
import time
from random import randrange
#Create socket as Publisher
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5556")

#Continuously send out a message every 5 seconds
while True:
    #print("Sending Message")
    zipcode = randrange(1, 100000)
    message = "Hello World!"
    #b = message.encode('utf-8')
    #socket.send(b)
    socket.send_string("%i*%s" % (zipcode, message))
    #print("Message sent")
    #time.sleep(10)
