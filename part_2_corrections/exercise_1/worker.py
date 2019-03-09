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
    message = socket.recv()
    pizza_ordered = message.decode("utf-8")
    print("Received request: " + pizza_ordered)

    # Make pizza
    time.sleep(5)

    # Get price
    pizza_with_price = ""
    for pizza in p.pizzas:
        if (pizza[0] == pizza_ordered):
            pizza_with_price = pizza[0]+", "+str(pizza[1]) + "€"
    # Send pizza
    print("Following order is ready : "+pizza_with_price)
    socket.send_string(pizza_with_price)
