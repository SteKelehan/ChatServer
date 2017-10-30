import socket
import time

# Creating a socket object! 
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Setting localhost! -> use function to fine local machine name and set port!
host = 'localhost'
port = 1234
BufferSize = 1024

# Get link to the port
serversocket.connect((host, port))

with open('Received_file.txt', 'wb') as f:
    print ('file opened')
    while (1):
        data = serversocket.recv(BufferSize)
        print('data ' + data )
        if not data:
            f.close()
            print( 'file closed' )
            break
        f.write(data)

print('Successfully get the file')
serversocket.close()
print('Connection Closed')


