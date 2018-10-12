import socket
import random
from threading import Thread
import datetime


kdc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
kdc_host =''
kdc_port =8080
kdc.connect((kdc_host,kdc_port))
a_id = 1
b_id = 2
private_key = None
public_key = None
kdc_shared_key = None
alice_key = None
confirmation_nonce = None

def dh():
    global private_key
    global public_key
    global kdc_shared_key
    # send prompt using to kdc to do diffie helman
    msg = 'dh1,' + str(b_id)
    kdc.send(msg.encode()) 
    # get generator, prime modulus, server's public key
    data = ''
    data = kdc.recv(1024).decode()
    kdc_modulus, kdc_gen, kdc_public_key = tuple(data.split(','))
    kdc_modulus = int(kdc_modulus)
    kdc_gen = int(kdc_gen)
    kdc_public_key = int(kdc_public_key)
    # generate public, private key and shared key
    private_key = random.randint(5,10)
    public_key = kdc_gen**private_key % kdc_modulus
    kdc_shared_key = kdc_public_key**private_key % kdc_modulus
    # send back public key
    msg = 'dh2,' + str(b_id) +','+ str(public_key)
    kdc.send(msg.encode())

# accept initial message to get shared key and check nonce
def ns1(msg, client):
    global alice_key
    global confirmation_nonce
    # decrypt original message
    d_msg = ''.join(chr(ord(a) ^ kdc_shared_key) for a in msg)
    d_msg = d_msg.split(',')
    timestamp = datetime.datetime.strptime(d_msg[2], '%Y:%m:%d %H:%M:%S')
    alice_key = int(d_msg[0])
    # use timestamp to stop replay attacks
    time_passed = (timestamp - datetime.datetime.now())/datetime.timedelta(minutes=1)
    if(abs(time_passed) > 10):
        print('timestamp out of date')
        return
    # send a confirmation nonce
    confirmation_nonce = random.randint(0,64)
    msg = str(confirmation_nonce ^ alice_key)
    print(msg)
    client.sock.send(msg.encode())

# This should basically be an all clear
def ns2(nonce):
    global confirmation_nonce
    global alice_key
    nonce = int(nonce) ^ alice_key
    if nonce == confirmation_nonce:
        confirmation_nonce = None
        print('connected with alice successfully')
    else:
        print('unsuccessful connection with alice')

dh()
# now start a server to receive from alice
host = ''
port = 8081

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((host, port))
class Client(Thread):
    def __init__(self, socket, address):
        Thread.__init__(self)
        self.sock = socket
        self.addr = address
        self.start()

    def run(self):
        while 1:
            data = self.sock.recv(1024).decode().split(',')
            if(data[0] == 'ns1'):
                ns1(data[1], self)
            if(data[0] == 'ns2'):
                ns2(data[1])


serversocket.listen(5)
print ('server started and listening')
while 1:
    clientsocket, address = serversocket.accept()
    Client(clientsocket, address)

kdc.close ()