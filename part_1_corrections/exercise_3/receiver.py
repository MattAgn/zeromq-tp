# Task sink
# Binds PULL socket to tcp://localhost:5558
# Collects results from workers via that socket

import sys
import time
import zmq

context = zmq.Context()

# Socket to receive messages on
receiver = context.socket(zmq.PULL)
receiver.bind("tcp://*:5558")

# Wait for start of batch (first message received means the work results are going to arrive)
s = receiver.recv()

# Start our clock now
tstart = time.time()

# receive work results
for task_nbr in range(20):
    s = receiver.recv()
    print(s.decode("utf-8") + " received from Bob")

# Calculate and report duration of batch
tend = time.time()
print("Total time since first receive: %d msec" % ((tend-tstart)*1000))
