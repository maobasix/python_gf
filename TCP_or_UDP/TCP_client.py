import socket

address = ('127.0.0.1', 9694)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect(address)
    print(type(s))
except:
    print("404 Not Found!!")
    exit()

while True:
    send_data = input("发送:")
    s.send(send_data.encode())
    data = s.recv(1024).decode()
    if send_data == 'exit':
        break
    if data == 'exit':
        break
    print('server:', data)
s.close()
