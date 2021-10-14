import argparse
import socket
import select
import sys

def client(ip, port, username):
    # Create the socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.settimeout(3)
    server.connect((ip, port))

    # We are waiting for input from the user typing or from the server connection
    read_list = [sys.stdin, server]

    # Create a flag for the loop
    running = True

    # Keep reading until exit is requested
    while running:
        # select() will wait for one of the sockets to be ready
        read_socket, write_socket, error_socket = select.select(read_list, [], [])

        for socks in read_socket:
            # Check if the server send us a message on the socket
            if socks == server:
                line = socks.recv(2048)
                if len(line) > 0:
                    # The server sent us an encrypted message.
                    print encryption.decrypt(line)
                else:
                    print 'FATAL: Server disconnected'
                    running = False
            # Else it was the user entering data
            else:
                line = sys.stdin.readline().strip()
                # Test for special commands
                if line == '/exit':
                    running = False
                # Else encrypt the message and send to the server
                elif len(line) > 0:
                    message = encryption.encrypt('%s> %s' % (username, line))
                    server.send(message)

    server.shutdown(socket.SHUT_RDWR)
    server.close()

# Default values
port = 8000
ip = '127.0.0.1'
username = 'Anonymous'

# Parse input arguments
parser = argparse.ArgumentParser()
parser.add_argument("--encryption", default='plaintext', help="Encryption algorithm to use")
parser.add_argument("--ip", help="Server IP address")
parser.add_argument("--key", help="Key to use for encryption")
parser.add_argument("--port", help="Server port")
parser.add_argument("--username", help="Username to use in chatroom")
args = parser.parse_args()

# Update default values with those provided by arguments
if args.port:
    port = int(args.port)

if args.ip:
    ip = args.ip

if args.username:
    username = args.username

if args.encryption == 'plaintext':
    import plaintext as encryption
elif args.encryption == 'caesar':
    # TODO: Import the caesar cipher module
else:
    raise Exception('Unknown encryption algorithm: %s', args.encryption)

# Start the client
client(ip, port, username)
