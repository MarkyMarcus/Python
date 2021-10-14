import argparse
import socket
import sys
import thread

def clientthread(conn, addr):
    '''
    Client thread for each connection
    '''
    while True:
        try:
            # Wait for a message from the client
            message = conn.recv(2048)

            if message:
                print "%s:%s -> %s" % (addr[0], addr[1], message)

                # Calls broadcast function to send message to all
                broadcast(message, conn)
            else:
                # message may have no content if the connection is broken, in this case we remove the connection
                print "%s:%s disconnected" % (addr[0], addr[1])
                clients.remove(conn)
                break

        except:
            continue


def broadcast(message, conn):
    '''
    Send a message to all clients that aren't the sending connection
    '''
    for c in clients:
        if c != conn:
            foo = c.send(message)


def server(ip, port):
    # Create the socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server.bind((ip, port))

    # listen for up to 100 connections
    server.listen(100)

    while True:
        # Accepts a connection request and stores two parameters, conn which is a socket object for that user, and addr
        # which contains the IP address of the client that just connected
        conn, addr = server.accept()

        # Maintains a list of clients for ease of broadcasting a message to all available people in the chatroom
        clients.append(conn)

        # prints the address of the user that just connected
        print "%s:%s connected" % (addr[0], addr[1])

        # creates and individual thread for every user that connects
        thread.start_new_thread(clientthread, (conn, addr))

    # Close all of the clients
    for c in clients:
        c.shutdown(socket.SHUT_RDWR)
        c.close()

    server.close()

# Default values
port = 8000
ip = '127.0.0.1'

# Create a list to hold all of the clients
clients = []

# Parse input from the user
parser = argparse.ArgumentParser()
parser.add_argument("--ip", help="Server IP address")
parser.add_argument("--port", help="Server port")
args = parser.parse_args()

# Update the default values with those from input
if args.port:
    port = int(args.port)

if args.ip:
    ip = args.ip

# Start the server
server(ip, port)
