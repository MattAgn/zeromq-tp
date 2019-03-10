# Installation

## Install Python

We'll be using Python for this presentation, if you dont't have it, check this : https://docs.python.org/3/using/windows.html

## Install the software

### Linux Ubuntu

Run linux_install.sh where you want to install the software

### Mac

Run `brew install zmq`.</br>
If you don't have brew, first run : </br>
`/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"`

### Windows

Download first package here : https://github.com/zeromq/pyzmq/downloads

## Install the python library

Run `pip install pyzmq`

# Useful links

Here is a detailed guide for zero-mq : http://zguide.zeromq.org/page:all</br>

Here are the Python docs for zero-mq : https://pyzmq.readthedocs.io/en/latest/api/zmq.html

# Exercises

## Part 1 : basic patterns

### Exercise 1 : basics client/server

The goal of this exercise is to use the basic functions of zeroMQ sockets to send and receive a hello world message.

The client creates a socket and connect it to the local host address via the port 5555, then sends 10 "Hello world" request messages and wait each time for a response.

The server creates a socket and binds it to the incoming connection via the port 5555, then waits for messages to arrive, for each message it receives it sends back a hello world response message.

### Exercise 2 : basiscs publisher/subscriber

The goal of this exercise is to establish a basic publish/subscribe connection between a server and a client.

The server receives connections via a socket bound to the port 5555. Generates random numbers to be used as topics and sends messages along with those generated topics.

The client creates subscribe type sockets and connect them to the corresponding addresses, then filter the received messages from the publishers with a specific topic, then performs some treatement on the information he received.

### Exercise 3 : workers

Let's suppose we have 3 people : Alice, Bob and Jean.

- Alice sends 20 numbers to the worker
- Bob is the worker
- Jean is the client waiting for the work

The task for Bob : get the square of each number Alice sends and transmit it to Jean.</br>
Bob will take 1 second to compute the square.

## Part 2 : advanced patterns

### Exercise 1 : broker

Let's suppose we run a pizzeria.

- Several clients order 1 pizza randomly from a given list
- Workers make the pizzas in 5 seconds (they're very good pizzaiolos) and send them back with their price
- The delivery takes 2 seconds

What kind of architecture would you use ?
Try to run 4 clients and 2 workers and see what happens

### Exercise 2 : forwarder

The goal of this exercise is to establish a publish/subscribe connection between subscribers and publishers via a device so that the subscribers won't have to know the addresses of the publishers.

The device will have a frontend and backend sockets, one for the publishers bound to the port 5559, and one for the subscribers bound to the port 55560.

The publishers will connect to the frontend socket and the subscribers to the backend socket.
The device will route the messages received on the frontend socket from publishers to the subscribers via the backend socket.
