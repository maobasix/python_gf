import socket

# 1.创建套接字
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 2.收发数据
target_ip = '127.0.0.1'
target_port = 8888
while True:
    send_data = input("发送：")
    s.sendto(send_data.encode(), (target_ip, target_port))
    if send_data == 'exit':
        break
    recv_data, server_addr = s.recvfrom(1024)
    recv_data = recv_data.decode()
    print("接收：", recv_data)
    if recv_data == 'exit':
        break
# 3.关闭套接字
s.close()

