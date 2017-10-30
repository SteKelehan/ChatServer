import socket
from threading import Thread
from SocketServer import ThreadingMixIn

#Creatring a TCP Server
#create a socket obj
host = 'localhost'
port = 1234
BufferSize = 1024

#################################
#                               #
#     Create a Thread class     #            
#                               #
#################################

class ClientThread(Thread):

    def __init__(self, ip, port, sock):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.sock = sock
        print("New thread IP: " + ip + "Port " + str(port))

    def run(self):
        filename = 'Testfile.txt'
        f = open(filename, 'rb')
        while (1):
            l = f.read(BufferSize)
            while(l):
                self.sock.send(l)
                l = f.read(BufferSize)
            if not l:
                f.close()
                self.sock.close()
                break

#setting up sockets
socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.setsockopt(level,optname, value) 
socket_tcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
socket_tcp.bind((host, port))
#creating an empty array of threads
threads= []

###############################################
#                                             #
#       Colecting data from client            #
#                                             #
###############################################

while 1:
    # Listen for connect to port 
    socket_tcp.listen(5)
    print("Awaiting connection \n")
    #Returning two values new sock obj and address of connection 
    (conn, (ip,port)) = socket_tcp.accept()
    print("Connected to IP: " + str(ip) + 'Port: ' + str(port))
    # Creadting new thread for multiple connections
    newthread = ClientThread(ip,port,conn)
    # starting a new thread
    newthread.start()
    # add to the list 
    threads.append(newthread)


for t in threads:
    t.join()



        

