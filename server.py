import socket
from threading import Thread
from SocketServer import ThreadingMixIn
import sys
import select


#Creatring a TCP Server
#create a socket obj
host = 'localhost'
port = 5678
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



def server():
    
    #setting up sockets
    socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # socket.setsockopt(level,optname, value) 
    socket_tcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    socket_tcp.bind((host, port))
    socket_tcp.listen(10)

    socket_list.append(socket_tcp)       # add server socket to tyhe list of readable connections
    print("Chat server started on Port: " + str(port) + " HostName: " + str(host))
    while True:
        # get the list of sockets
        # 4th argument, timeout = 0 :poll and never block
        ready_to_read, ready_to_write, in_error = select.select(socket_list, [ ],[ ], 0)

        for sock in ready_to_read:
            # a new connection request recived
            if sock == socket_tcp:
                sockfd, addr = socket_tcp.accept()
                socket_list.append(sockfd)
                print("Connected")

                broadcast(socket_tcp, sockfd, str(addr) + " : " + str(addr) + " entered the chat room\n")
            else:
                try:
                     # process data taken form client
                     data = sock.recv(RECV_BUFFER)
                     if data:
                         #there is somthing in socket
                         broadcast(socket_tcp, sock, "\r" + "[" + str(sock.getpeername()) + "] " + data)
                     else:
                         if sock in socket_list:
                             socket_list.remove(sock)

                         # this means that the connect is prob broken! thus close connection
                         broadcase(socket_tcp,sock, "Client " + str(addr) + " : " + str(addr) + " is offline")

                except:
                    broadcast(socket_tcp,"Client " + addr + " : " + addr + " is offline")
                    continue
            socket_tcp.close()



def broadcast (server_socket, sock, message):
    for socket in socket_list:
        # send message to spespic person
        if socket != server_socket and sock != sock :
            try:
                socket.send(message)
            except:
                #broken socket connection
                socket.close()
                if socket in socket_list:
                    socket_list.remove(socket)

if __name__ == "__main__":
    sys.exit(server())


    














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



        

