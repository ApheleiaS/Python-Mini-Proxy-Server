import sys
import socket

print "Welcome to Proxy Server!"
proxy_port = 8080
num_args = len(sys.argv)
if (num_args-1):
    proxy_port = int(sys.argv[1])
    print "Starting Proxy Server on port: " + sys.argv[1]
else: 
    print "Port Number for Proxy Server Not Specified. Using 8080"


def create_bind_listen_socket(sock, port_num): 
    #create socket 
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error, msg:
        print 'Failed to create socket. Error code: ' + str(msg[0]) + ' ,Error message : ' + msg[1]
        sys.exit();
    #bind to port_num 
    #Bind socket to local host and port
    try:
        sock.bind(("127.0.0.1", port_num))
    except socket.error as msg:
        print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()
 
    #Start listening on socket
    sock.listen(10)
    print 'Socket now listening'
 
    #now keep talking with the client
    while 1:
        #wait to accept a connection - blocking call
        conn, addr = sock.accept()
        print 'Connected with ' + addr[0] + ':' + str(addr[1])

sock = ""
create_bind_listen_socket(sock, proxy_port)
