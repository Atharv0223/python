import socket
from threading import Thread
c = socket.socket()
c.connect(('localhost',9999))
msg,rpl = ("","")
def send():
    msg=""
    while msg!="bye":
        msg = input("your msg :\t")
        msg = c.send(bytes(msg,'utf-8'))
    
        
def receive():
    rpl=""
    while rpl!="bye":
        rpl = c.recv(1024).decode()
        print(f"Server :\t{rpl}")
t1 = Thread(target = send)
t2 = Thread(target = receive)
t1.start()
t2.start()
t1.join()
t2.join()