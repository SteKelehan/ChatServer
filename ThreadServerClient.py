import socket
import threading 
import SocketServer


class ThreadedRequHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        data = str(self.request.recv(1024))
        thread = threading.current_thread()
        response = bytes("{}: {}".format(thread.name ,data))
        self.request.sendall(response)




class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

def client(ip,port,message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    try:
        sock.sendll(bytes(message))
        response = str(sock.recv(1024))
        print("Received: {}".format(responce))
    finally:
        sock.close()


if __name__ == "__main__":
    host, port = "localhost", 0
    
    server = ThreadedTCPServer((host,port), ThreadedRequHandler)
    ip, port = server.server_address

    # start a thread with the server
    # the thread will then startt on more thread for each request
    server_thread = threading.Thread(target=server.serve_forever)

    # exit the server thread when the main thread terminates
    server_thread.daemon = True
    server_thread.start()
    print("Server loop running in thread: " + server_thread.name)

    client(ip, port, "Hello World 1")
    client(ip, port, "Hello World 2")
    client(ip, port, "Hello World 3")

    server.shutdown()



