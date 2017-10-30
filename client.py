import socket

#create a socket obj
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()

port = 9999

#Connect to hostname
s.connect((host,port))

# Resve limit no. of bytes! -> this instance 1024
mess = s.recv(1024)
s.close()

print("The time got from server is " + mess.decode('ascii'))


