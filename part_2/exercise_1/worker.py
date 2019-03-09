#   Pizza delivery man
#   Request-reply service in Python
#   Connects REP socket to tcp://localhost:5560
#   Expects pizza name from broker and sends price

import zmq
import time
import pizzas as p

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.connect("tcp://localhost:5560")

while True:
    # TODO: handle pizza order
