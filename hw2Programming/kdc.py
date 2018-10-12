import socket
import random
import datetime
from threading import Thread

host = ''
port = 8080

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((host, port))
# stores servers private key, public, and other public and shared key    
id_to_publickey = {}
modulus = 19
gen = 3

# return generator, prime modulus, server's public key
# store private key, server's public key
def dh1(id, client):
    s_key = random.randint(5,10)
    p_key = gen**s_key % modulus
    # secret key, public key, other public key, joint key
    id_to_publickey[id] = {'s_key' : s_key, 'p_key' : p_key, 'o_p_key' : None, 
                            'j_key' : None}
    to_sent = str(modulus) + ',' + str(gen) + ',' + str(p_key)
    client.sock.send(to_sent.encode())
    

# store shared key computed from other's public key
def dh2(id, public_key):
    j_key = public_key**id_to_publickey[id].get('s_key') % modulus
    id_to_publickey[id]['o_p_key'] = public_key
    id_to_publickey[id]['j_key'] = j_key


# return Eka: [Ks, id b, nonce1, (Ekb: [Ks, id a, nonce2] )]
def ns(id1, id2, nonce, client):
    key_to_distrubute = random.randint(0,64)
    # make the message for id2
    msg_2 = str(key_to_distrubute) + ',' + id1 + ',' + \
            datetime.datetime.now().strftime('%Y:%m:%d %H:%M:%S')
    # get keys
    key_2 = id_to_publickey[id2].get('j_key')
    key_1 = id_to_publickey[id1].get('j_key')
    # encrypt message for id2
    e_msg2 = ''.join(chr(ord(a) ^ key_2) for a in msg_2)
    # make and encrypt message for id1
    msg_1 = str(key_to_distrubute) + ',' + id2 + ',' + nonce + ',' + e_msg2
    e_msg1 = ''.join(chr(ord(a) ^ key_1) for a in msg_1)
    # send message back
    client.sock.send(e_msg1.encode())


class Client(Thread):
    def __init__(self, socket, address):
        Thread.__init__(self)
        self.sock = socket
        self.addr = address
        self.start()

    def run(self):
        while 1:
            data = self.sock.recv(1024).decode().split(',')
            if(data[0] == 'dh1'):
                dh1(data[1], self)
            if(data[0] == 'dh2'):
                dh2(data[1], int(data[2]))
            if(data[0] == 'ns'):
                ns(data[1], data[2], data[3], self)


serversocket.listen(5)
print ('server started and listening')
while 1:
    clientsocket, address = serversocket.accept()
    Client(clientsocket, address)


# For dh send: dh and its id then 
# return generator, prime modulus, server's public key
# alice computer their public key and both parties compute shared key

# For ns send: ns ida, idb, nonce1
# return Eka: [Ks, id b, nonce1, (Ekb: [Ks, id a, nonce2] )]
