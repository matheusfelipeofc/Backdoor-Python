import socket
import sys
from time import sleep


c_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = sys.argv[1]
porta = int(sys.argv[2])

try:
    c_socket.connect((ip, porta))
except (ConnectionError, socket.error):
    print(f'Houve um erro ao se conectar a {ip}:{porta}')
    for c in range(3):
        try:
            c_socket.connect((ip, porta))
        except (ConnectionError, socket.error):
            print(f'Tentativa {c+1} de se reconectar falhada')
            sleep(1)
        else:
            break
else:
    while True:
        data = c_socket.recv(4096)
        print(data.decode())
        terminal = str(input(f'rce@noname404:~$ '))
        if terminal == '':
            c_socket.send(' '.encode())
        else:
            c_socket.send(terminal.encode())
        
        
    