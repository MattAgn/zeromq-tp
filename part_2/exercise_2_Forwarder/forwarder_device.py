import zmq


def main():

    try:
        context = zmq.Context(1)
        # Socket facing clients
		# TODO : Here instantiate the frontend socket ( of type sub)
		#		 binds it to the port 5559

        
        # Socket facing services
		# TODO : Here instantiate the backend socket ( of type pub)
		#		 binds it to the port 5560

		# TODO : Here add a device that connects the frontkend to the backtend
		
    except Exception, e:
        print e
        print "bringing down zmq device"
    finally:
        pass  
        # TODO : close the backend and frontend sockets at the end of the program 
        context.term()

if __name__ == "__main__":
    main()