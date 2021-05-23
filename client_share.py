''''This is the server side code for transfering file from the server to a client '''
import socket
import sys
import os
argv=sys.argv
C_IP=argv[1]
C_PORT=int(argv[2])
C_ADDR=(C_IP,C_PORT)
while True:
    C_socket=socket.socket()
    C_socket.connect(C_ADDR)
    end=C_socket.recv(2048)
    path=input('source path: ')
    C_socket.send(path.encode())
    path = os.path.join("download",path)
    with open(path, 'wb') as file:
        while True:
            lines=C_socket.recv(2048)
            if lines !=end:
                file.write(lines)
            else:
                C_socket.send(b'Done')
                break
        C_socket.close()
        print('File Downloaded to',path)
