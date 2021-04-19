import sys
import socket
import os
argv = sys.argv
if len(argv) == 3:
    IP = argv[1]
    PORT = int(argv[2])
    ADDR = (IP,PORT)
    END=b'BYE'
    print('heya')
    try:
        print('all good here')
        S_socket=socket.socket()
        S_socket.bind(ADDR)
        while True:
            S_socket.listen()
            print('ready for connection')
            C_socket,C_ADDR = S_socket.accept()
            print('connected to client at ',ADDR)
            C_socket.send(END)
            path = C_socket.recv(2048).decode()
            path = os.path.join(os.getcwd(),'repo',path)
            if os.access(path, os.R_OK):
                print('access allowed - ')
                with open(path,'rb') as file:
                    while True:
                        for line in file:
                            C_socket.send(line)
                        break
                    C_socket.send(END)
                    print('done')
                    C_socket.close()
            else: 
                print('access denied')
                    
    except Exception as error:
        print('error!!',error)
