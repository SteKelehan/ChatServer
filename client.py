import socket

#create a socket obj
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = socket.gethostname()

port = 1234

#Connect to hostname
s.connect((host,port))
s.send("Hello server!")

with open('file_received','wb') as f:
    print('file opened')
    while 1:
        print('receiving data ..')
        data = s.recv(1024)
        print('data ' + data)
        if not data:
            break
        #write data to a file
        f.write(data)

f.close()
print('Successfully got the file')
s.close()
print('connection closed')

