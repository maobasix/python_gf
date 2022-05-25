import socket
import json

s = socket.socket()
s.bind(('127.0.0.1', 9494))
s.listen()
conn, client_access = s.accept()  # 建立链接

while True:
    json_msg = json.loads(conn.recv(1024).decode('utf-8'))  # 接受文件属性，创建文件
    print('文件名为：{}，文件大小：{}'.format(json_msg['filename'], json_msg['filesize']))
    with open(json_msg['filename'], mode='wb') as f:
        content = conn.recv(json_msg['filesize'])
        print('接收到的数据大小:', len(content))
        f.write(content)

    conn.close()
    break
s.close()
