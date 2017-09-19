#Subscriber: Whenever a message is heard, print message

import zmq
import sys

#Creat port number for subscriber
port = "8888"
if len(sys.argv) > 1:
    port = sys.argv[1]
    int(port)

#Create socket as Subscriber
context = zmq.Context()
socket = context.socket(zmq.SUB)

#Connect to Publisher and subscribe
print("Connecting to Pub")
socket.connect("tcp://localhosts:%s" % port)
zip_filter = sys.argv[1] if len(sys.argv) > 1 else "10001"
if isinstance(zip_filter, bytes):
    zip_filter = zip_filter.decode('ascii')
socket.setsockopt_string(zmq.SUBSCRIBE, zip_filter)
print("Connected to Pub")

#print message
while True:
    print("Waiting for Message")
    b = socket.recv()
    print("Message received")
    message = b.decode('utf-8')
    print(message)







