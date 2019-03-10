import sys
import zmq

port = "5556"
if len(sys.argv) > 1:
    port =  sys.argv[1]
    int(port)
    
if len(sys.argv) > 2:
    port1 =  sys.argv[2]
    int(port1)

#	Socket to talk to server
context = zmq.Context()

#	TODO : create a socket of type zmq.SUB


print "Collecting updates from weather server..."
#	TODO :  connect the socket to tcp://localhost:port you need to check if there is more than one 
#			publisher. Use the ports defined in the variables port and port1.

#
#	zmq supports filtering of messages based on topics at subscriber side. This is usually set via socketoption
#

#	TODO :  Subscribe to a topic ( a zip code : integer) 
#			use the zip code to filter the messages, for that use the function setsockopt.

#	TODO :  get the topic and the data of the filtered messages received, 
#			print it, then calculate the average total value received and print it.

      
