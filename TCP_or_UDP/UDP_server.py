import socket

# 1.创建套接字
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # ipv4+udp
# 2.绑定端
ip = '127.0.0.1'
port = 8888
s.bind((ip, port))  # 地址必须是元组
# 3.收发数据
while True:
    # 接受数据
    recv_data, client_addr = s.recvfrom(1024)
    recv_data = recv_data.decode()
    print("接收：", recv_data)
    if recv_data == 'exit':
        break
    # 发送数据
    send_data = input("发送：")
    s.sendto(send_data.encode(), client_addr)
    if send_data == 'exit':
        break
# 4.关闭套接字
s.close()
