import socket
from threading import Thread
s = socket.socket()
s.bind(('localhost',9999))
s.listen()
while True:
    print('Waiting for connection')
    c,cadd=s.accept()
    print('connected with client at ',cadd)
    def send():
        cmsg=""
        while cmsg!="bye":
            cmsg = c.recv(1024).decode()
            print(f'Client msg:\t{cmsg.ljust(10)}')
    def receive():
        msg=""
        while msg!="bye":
            msg = input("Your msg :\t")
            c.send(bytes(msg,'utf-8'))
    t1 = Thread(target = send)
    t1.start()
    t2 = Thread(target = receive())
    t2.start()
    t1.join()
    t2.join()