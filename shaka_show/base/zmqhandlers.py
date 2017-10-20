import zmq

# Subscriber: Whenever a message is heard, print message

from zmq.eventloop import zmqstream


def get_command(msg):
    command = msg[0].decode('UTF-8')
    print("Received control command: %s" % command)


def zmq_sub(port_sub = "8080"):
    context = zmq.Context()
    socket_sub = context.socket(zmq.SUB)
    socket_sub.connect("tcp://localhost:%s" % port_sub)
    socket_sub.setsockopt_string(zmq.SUBSCRIBE, "")
    stream_sub = zmqstream.ZMQStream(socket_sub)
    stream_sub.on_recv(get_command)
    print("Connected to publisher with port %s" % port_sub)

