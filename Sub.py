#Subscriber: Whenever a message is heard, print message

import zmq
import sys

#Create socket as Subscriber
context = zmq.Context()
socket = context.socket(zmq.SUB)

#Connect to Publisher and subscribe
print("Connecting to Pub")
socket.connect("tcp://localhost:5556")

zip_filter = sys.argv[1] if len(sys.argv) > 1 else "10001"
if isinstance(zip_filter, bytes):
    zip_filter = zip_filter.decode('ascii')
socket.setsockopt_string(zmq.SUBSCRIBE, zip_filter)
print("Connected to Pub")

#print message
while True:
    print("Waiting for Message")
    string = socket.recv_string()
    zipcode, message = string.split('*')
    print("Message received")
    print(message)







