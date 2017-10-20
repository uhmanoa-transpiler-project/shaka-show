from zmqhandlers import zmq_sub

commList = zmq_sub(5558)
print("\n\nCommand List: ")
for i in range (0, len(commList)):
    print(commList[i])