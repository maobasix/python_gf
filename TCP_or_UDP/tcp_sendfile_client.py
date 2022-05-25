import os
import json
import socket

sk = socket.socket()
sk.connect(('127.0.0.1', 9494))

abs_path = r'C:\Users\maobasix\Desktop\笔记\信息安全三级考试笔记\main.md'  # 要发送的文件文件路径

filename = os.path.basename(abs_path)  # 获取文件名

filesize = os.path.getsize(abs_path)  # 获取文件大小
dic = {'filename': filename, 'filesize': filesize}
str_dic = json.dumps(dic)
sk.send(str_dic.encode('utf-8'))

with open(abs_path, mode='rb') as f:
    content = f.read()
    sk.send(content)

sk.close()
