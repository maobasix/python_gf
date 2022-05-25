import threading
import socket


def TCP_UP():
    while True:
        send_data = input("发送:")
        s.send(send_data.encode())
        if send_data == 'exit':
            break
    s.close()


def TCP_DOWN():
    while True:
        data = s.recv(1024).decode()
        if data == 'exit':
            break
        print("server:", data)
    # s.close()


if __name__ == '__main__':
    address = ('127.0.0.1', 9494)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect(address)
        print(type(s))
    except:
        print("404 Not Found!!")
        exit()
    t = threading.Thread(target=TCP_UP, name='TCP_UP').start()
    t2 = threading.Thread(target=TCP_DOWN, name='TCP_DOWN').start()
