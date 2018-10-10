import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host =''
port =8080
s.connect((host,port))

def ts(msg):
   s.send(msg.encode()) 
   data = ''
   data = s.recv(1024).decode()
   print (data)

while 2:
   r = input('enter: ')
   ts(r)

s.close ()