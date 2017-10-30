import socket
from threading import Thread
from SocketServer import ThreadingMixIn
import sys
import select

def client():
    # if the length of the command line arg is less than 3 -> exit
    if (len(sys.argv) < 3):
        print (" Usage : puthon chat_client.py hostname port")
        sys.exit()

    #the host name is the first command line argument
    host = sys.argv[1]
    #the port is the second command line aregument
    port = sys.argv[2]
    
    print( "Host: " + host + " Port: " + port)


    # Set up socket and set it to time out
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #s.settimeout(2)

    #connect to client/host
    try:
        s.connect((host,port))
    except:
        print("Unable to connect to host")
        sys.exit()

    print("Connect to remot host, You can start to chat! Woooo")
    # Print to comandline forces the buffer to be flushed and writes everything in the buffer even if it woulf wait nomally
    sys.stdout.write('[Me] '); sys.stdout.flush()
    
    while True:
        socket_list = [sys.stdin, s]
        
        # Get list of sockets which are readable
        ready_to_read,ready_to_write,in_error = select.select(socket_list, [] , [])

        for sock in ready_to_read:
            if sock == s:
                # incoming message from remote server, s
                data = sock.recv(4096)
                if not data:
                    print("\nDisconnected form chat server")
                    sys.exit()
                else:
                    # Print the data
                    sys.stdout.write(data)
                    sys.stdout.write("[Me] "); sys.stdout.flush()
            else:
                # get message user have entered
                message = sys.stdin.readline()
                s.send(message)
                sys.stdout.write("[Me] "); sys.stdout.flush()


if __name__ == "__main__":
    sys.exit(client())
