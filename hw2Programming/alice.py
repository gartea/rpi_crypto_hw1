import socket
import random

# connect to kdc
kdc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
kdc_host =''
kdc_port =8080
kdc.connect((kdc_host,kdc_port))
# connect to bob
bob = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
bob_host =''
bob_port =8081
bob.connect((bob_host,bob_port))
a_id = 1
b_id = 2
private_key = None
public_key = None
kdc_shared_key = None
bob_key = None
ns_nonce_gotten = False

def dh():
    global private_key
    global public_key
    global kdc_shared_key
    # send prompt using to kdc to do diffie helman
    msg = 'dh1,' + str(a_id)
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
    msg = 'dh2,' + str(a_id) +','+ str(public_key)
    kdc.send(msg.encode())

def ns():
    global bob_key
    global ns_nonce_gotten
    # get data from kdc to send to bob
    nonce = random.randint(1,64)
    msg = 'ns,' + str(a_id) + ',' + str(b_id) + ',' + str(nonce)
    kdc.send(msg.encode())

    data = ''
    data = kdc.recv(1024).decode()
    # receive message back with the requisite and decrypt it
    d_data = ''.join(chr(ord(a) ^ kdc_shared_key) for a in data)
    d_data = d_data.split(',')
    # see if anything gotten back from kdc is wrong
    if ns_nonce_gotten or int(d_data[2]) != nonce or b_id != int(d_data[1]):
        print('bad nonce')
        return
    ns_nonce_gotten = True
    bob_key = d_data[0]
    for_bob = 'ns1,' + ''.join(d_data[3:])
    # Now send this to bob
    bob.send(for_bob.encode())
    # get return nonce
    data = ''
    data = bob.recv(1024).decode()
    print('connection with bob confirmed from alice')
    msg = 'ns2,' + data
    bob.send(msg.encode())


dh()
ns()

kdc.close ()