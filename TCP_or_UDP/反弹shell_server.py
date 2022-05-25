import socket
from subprocess import Popen, PIPE

rest = socket.socket()
ip = '127.0.0.1'
port = 9694
rest.bind((ip, port))
rest.listen()
conn, client_access = rest.accept()  # 接收数据
while True:
    recv_data = conn.recv(1024)
    recv_data = recv_data.decode()
    if recv_data == 'exit':
        break
    cmd = Popen(['/bin/bash', '-c', recv_data], stdin=PIPE, stdout=PIPE)
    result = cmd.stdout.read()
    conn.send(result)
    # conn.send(send_data.encode())
rest.close()
