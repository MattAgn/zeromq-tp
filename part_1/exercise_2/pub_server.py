import zmq
import random
import sys
import time


#	Publishers are created with ZMQ.PUB socket types

port = "5556"
if len(sys.argv) > 1:
    port =  sys.argv[1]
    int(port)

context = zmq.Context()

#	TODO :  Create a publisher with the socket type zmq.PUB.
#			Bind it to : tcp://*:port ( use the variable port to complete the adress ).



#	Data is published along with a topic. 
#	The subscribers usually sets a filter on these topics for topic of their interests.

while True:
	# TODO : Generate a random number for the topic ( you can use random.randrange ).
	#	 Send a message under that topic and sleep for some time ( you can use time.sleep ).
	
