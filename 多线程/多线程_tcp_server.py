import socket
import threading


def TCP_DOWN():

    while True:
        recv_data = conn.recv(1024)
        recv_data = recv_data.decode()
        print("client:", recv_data)
        if recv_data == 'exit':
            break
    conn.close()
    s.close()


def TCP_UP():
    while True:
        message = input("发送：")
        send_data = message  # 发送数据
        conn.send(send_data.encode())
        if send_data == 'exit':
            conn.close()
            s.close()


if __name__ == '__main__':
    port = ('127.0.0.1', 9494)
    s = socket.socket()
    s.bind(port)
    s.listen()
    conn, client_access = s.accept()
    t = threading.Thread(target=TCP_UP, name='TCP_DOWN').start()
    t2 = threading.Thread(target=TCP_DOWN, name='TCP_UP').start()
