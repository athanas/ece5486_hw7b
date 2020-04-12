#/usr/bin/python

#########################################################################
#
#  FILE: relay_ipv6.py
#
#  DESCRIPTION: The purpose of this recipe is to gather packets from node 
#      N2 and carry them over to node N3 as expediently as possible.
#
#  CREATED: <unfinished>
#
#########################################################################

#
#  THIS LOOKS A LOT LIKE GATHERER_IPV6.PY.  MODIFY THIS SO THAT IT PERFORMS
#  THE RELAY FUNCTION
#

import socket
import sys
import struct
from subprocess import check_output

LISTEN_PORT = 10000

# Determine my IPV6 address:
myIP = check_output(['hostname', '-I']).split()[1]
print("My IPV6 address is "+myIP)

server_address = (myIP, 10000, 0, 0)

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM, 0)

# Bind the socket to the port
sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)

print("Ready for action.")
pktcount = 0

while True:
    # Wait for a connection
    connection, client_address = sock.accept()
    try:
        print >>sys.stderr, 'connection from', client_address

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(4096)
            if not data:
                print >>sys.stderr, 'no more data from', client_address
                break
            flowId = struct.unpack('>I',data[4:8])[0]
            if flowId != 1: continue
            seq = struct.unpack('>I',data[8:12])[0]
            pktcount+=1
            print(myIP+": From "+str(client_address[0])+": SEQ  = "+str(seq)+ " PKTCOUNT: "+str(pktcount))


    finally:
        # Clean up the connection
        print("All done.  A total of "+str(pktcount)+" packets were successfully received.")
        connection.close()

