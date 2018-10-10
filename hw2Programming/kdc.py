import socket
from threading import *

host = ''
port = 8080

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((host, port))

class client(Thread):
    def __init__(self, socket, address):
        Thread.__init__(self)
        self.sock = socket
        self.addr = address
        self.start()

    def run(self):
        while 1:
            print('Client sent:', self.sock.recv(1024).decode())
            self.sock.send(b'You sent something to me')

serversocket.listen(5)
print ('server started and listening')
while 1:
    clientsocket, address = serversocket.accept()
    client(clientsocket, address)


# For dh send: dh and its id then 
# return generator, prime modulus, server's public key
# alice computer their public key and both parties compute shared key

# For ns send: ns ida, idb, nonce1
# return Eka: [Ks, id b, nonce1, (Ekb: [Ks, id a, nonce2] )]
