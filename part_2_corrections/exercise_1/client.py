#
#   Request-reply client in Python
#   Connects REQ socket to tcp://localhost:5559
#   Sends "Hello" to server, expects "World" back
#
import zmq
import pizzas as p
from random import randint

#  Prepare our context and sockets
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5559")

# Order and receive pizza
pizza_ordered = p.pizzas[randint(0, len(p.pizzas) - 1)]
socket.send_string(pizza_ordered[0])
print("Client ordered a "+pizza_ordered[0])
pizza_and_price = socket.recv()
print("Client received its pizza : " + pizza_and_price.decode("utf-8"))
