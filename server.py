import socket
from threading import Thread
from SocketServer import ThreadingMixIn
import sys
import select



#Creatring a TCP Server
#create a socket obj
host = ''
port = 9000
BufferSize = 4096
socket_list = []

#################################
#                               #
#     Create a Thread class     #            
#                               #
#################################

#class ClientThread(Thread):
#
#    def __init__(self, ip, port, sock):
#        Thread.__init__(self)
#        self.ip = ip
#        self.port = port
#        self.sock = sock
#        print("New thread IP: " + ip + "Port " + str(port))
#
#    def run(self):
#        filename = 'Testfile.txt'
#        f = open(filename, 'rb')
#        while (1):
#            l = f.read(BufferSize)
#            while(l):
#                self.sock.send(l)
#                l = f.read(BufferSize)
#            if not l:
#                f.close()
#                self.sock.close()
#                break


def chat_server():

    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    tcp_socket.bind((host, port))
    tcp_socket.listen(10)
 
    # add server socket object to the list of readable connections
    socket_list.append(tcp_socket)
 
    print "Chat server started on port " + str(port)
 
    while 1:

        # get the list sockets which are ready to be read through select
        # 4th arg, time_out  = 0 : poll and never block
        ready_to_read,ready_to_write,in_error = select.select(socket_list,
                                                                       [],
                                                                       [],
                                                                       0
                                                                       )
        for sock in ready_to_read:
            # a new connection request recieved
            if sock == tcp_socket: 
                sockfd, addr = tcp_socket.accept()
                socket_list.append(sockfd)
                print "Client (%s, %s) connected" % addr
                 
                broadcast(tcp_socket, 
                              sockfd,
                              "[%s:%s] entered our chatting room\n" % addr
                              )
             
            # a message from a client, not a new connection
            else:
                # process data recieved from client, 
                try:
                    # receiving data from the socket.
                    data = sock.recv(BufferSize)
                    if data:
                        if data == "HELO text\n":
                            sock.send("\r" + '[' + str(sock.getpeername()) + '] ' 
                                            + data + "IP:[" + str(sock.getpeername()) + ']\n' + 'Port:[' + str(port) + ']\n' + 'StudentID:[14316006]\n'
                                            )
                        else:
                            broadcast(tcp_socket,
                                             sock,
                                             "\r" + '[' + str(sock.getpeername()) + '] ' + data
                                             )  
                        # there is something in the socket
                    else:
                        # remove the socket that's broken    
                        if sock in socket_list:
                            socket_list.remove(sock)

                        # at this stage, no data means probably the connection has been broken
                        broadcast(tcp_socket,
                                        sock,
                                        "Client (%s, %s) is offline\n" % addr
                                        ) 

                # exception 
                except:
                    broadcast(tcp_socket,
                                    sock,
                                    "Client (%s, %s) is offline\n" % addr
                                    )
                    continue

    tcp_socket.close()
    
# broadcast chat messages to all connected clients
def broadcast (tcp_socket, sock, message):
    for socket in socket_list:
        # send the message only to peer
        if socket != tcp_socket and socket != sock :
            try :
                socket.send(message)
            except :
                # broken socket connection
                socket.close()
                # broken socket, remove it
                if socket in socket_list:
                    socket_list.remove(socket)
 
if __name__ == "__main__":
    sys.exit(chat_server())

    














#setting up sockets
#socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.setsockopt(level,optname, value) 
#socket_tcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#socket_tcp.bind((host, port))
#creating an empty array of threads
#threads= []

###############################################
#                                             #
#       Colecting data from client            #
#                                             #
###############################################

#while 1:
#    # Listen for connect to port 
#    socket_tcp.listen(5)
#    print("Awaiting connection \n")
#    #Returning two values new sock obj and address of connection 
#    (conn, (ip,port)) = socket_tcp.accept()
#    print("Connected to IP: " + str(ip) + 'Port: ' + str(port))
#    # Creadting new thread for multiple connections
#    newthread = ClientThread(ip,port,conn)
#    # starting a new thread
#    newthread.start()
#    # add to the list 
#    threads.append(newthread)


#for t in threads:
#    t.join()



        

