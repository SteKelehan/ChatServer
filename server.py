import socket
import time


#Creating a socket object! 
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Setting localhost! -> use function to fine local machine name and set port!
host = socket.gethostname()

port = 9999

# Get link to the port
serversocket.bind((host, port))

# Execpt 5 requests -> use listen, listens for connects to the socket
serversocket.listen(5)

while 1:
    #connection, get and print address 
    clientsocket,addr = serversocket.accept()
    #accept() -> returns two values, one new socket obj and the address of the connection
    print("Have connection with " + str(addr))
    currentTime = time.ctime(time.time()) + "\r\n"
    clientsocket.send(currentTime.encode('ascii'))
    clientsocket.close()


