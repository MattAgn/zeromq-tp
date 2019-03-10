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

# Exercises

## Part 1 : basic patterns
### Exercise 1 : basics client/server
The goal of this exercise is to use the basic functions of zeroMQ sockets to send and receive a hello world message.
The client creates a socket of its own and connect it to the local host address via the port 5555, then sends request messages wait each time for a response.
The server creates a socket and binds it to the incoming connections via the port 5555, then waits for messages to arrive, for each message it receives it sends back a hello world response message.


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

- Several clients order 1 pizza randomly from the given list
- Workers (pizzaiolos) make the pizzas in 5 seconds (they're very good pizzaiolos) and send them back with their price
- The delivery takes 2 seconds

Try to run 4 clients and 2 workers and see what happens
