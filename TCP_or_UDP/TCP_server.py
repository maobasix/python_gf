import socket

rest = socket.socket()
ip = '127.0.0.1'
port = 9694
rest.bind((ip, port))
rest.listen()
conn, client_access = rest.accept()  # 接收数据
while True:
    recv_data = conn.recv(1024)
    recv_data = recv_data.decode()
    print("client:", recv_data)
    if recv_data == 'exit':
        break

    send_data = input("发送：")  # 发送数据
    conn.send(send_data.encode())
    if send_data == 'exit':
        conn.close()
        break
rest.close()
