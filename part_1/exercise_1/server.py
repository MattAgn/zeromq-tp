#
#   Hello World server in Python
#   Binds REP socket to tcp://*:5555
#   Expects b"Hello" from client, replies with b"World"
#

import time
import zmq

context = zmq.Context()

#	TODO : Here create a socket and bind it to tcp://*:5555


while True:
    #  TODO : Wait for next request from client
	#  TODO : Get the message from the client 
	#  TODO : wait some time ( you can use the function sleep of the package time )
	#  TODO : Send a reply back to the client  
