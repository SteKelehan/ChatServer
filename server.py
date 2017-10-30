import socket
import time


#Creating a socket object! 
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Setting localhost! -> use function to fine local machine name and set port!
host = socket.gethostname()

port = 1234

# Get link to the port
serversocket.bind((host, port))

# Execpt 5 requests -> use listen, listens for connects to the socket
serversocket.listen(5)

print ('Server wating for connection..... ')

while 1:
    #connection, get and print address 
    clientsocket,addr = serversocket.accept()
    #accept() -> returns two values, one new socket obj and the address of the connection
    print("Have connection with " + str(addr))
    data = clientsocket.recv(1024)
    print('Server resived' + repr(data))
    
    #open a file and read 1024 bytes at a time
    filename = 'Testfile.txt'
    f = open(filename,'rb')
    l = f.read(1024)
    while(l) :
        #Sending line read from texty file l -> 1024 
        clientsocket.send(l)
        print('Sent' , repr(l))
        print('\n')
        l = f.read(1024)
    f.close()

    print('Finished Sending')
    clientsocket.send('Thanks')
    clientsocket.close()


