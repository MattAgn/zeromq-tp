import zmq
import time

# Prepare our context and sockets
context = zmq.Context()
frontend = context.socket(zmq.ROUTER)
backend = context.socket(zmq.DEALER)
frontend.bind("tcp://*:5559")
backend.bind("tcp://*:5560")

# Initialize poll set
poller = zmq.Poller()
poller.register(frontend, zmq.POLLIN)
poller.register(backend, zmq.POLLIN)

while True:
    socks = dict(poller.poll())

    if socks.get(frontend) == zmq.POLLIN:
        # TODO: transmit pizza order
        print("Transmitting pizza order : ")

    if socks.get(backend) == zmq.POLLIN:
        # TODO: deliver pizza to client
        print("Delivered order : ")
