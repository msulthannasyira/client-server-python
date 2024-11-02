import socket
import sys
import argparse

host = '192.168.38.60'
data_payload = 2048

def echo_client(port):
    """ A simple echo client """
    
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    server_address = (host, port)
    print("Connecting to %s port %s" % server_address)
    
    message = 'This is the message. It will be repeated.'
    
    try:
        # Send data
        print("Sending %s" % message)
        sent = sock.sendto(message.encode('utf-8'), server_address)
        
        # Receive response
        data, server = sock.recvfrom(data_payload)
        print("Received: %s" % data.decode('utf-8'))
    
    finally:
        print("Closing connection to the server")
        sock.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Socket Client Example')
    parser.add_argument('--port', action="store", dest="port", type=int, required=True)
    given_args = parser.parse_args()
    
    port = given_args.port
    echo_client(port)
