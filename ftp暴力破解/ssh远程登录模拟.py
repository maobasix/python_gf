# -*- coding:utf-8 -*-
# @Time :  19:02
# @Author : yangguoping
# @File : .py
# @software :
# paramiko--ssh远程登录模块
import paramiko


def telent_ssh(ip, prot, user, pwd):
    client = paramiko.SSHClient()  # 创建sshHClient
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 允许链接不在Known_host文件中的主机
    try:
        client.connect(ip, prot, user, pwd)  # 连接服务器
        print('登录成功')

    except :
        print('登录失败')

    client.close()  # 关闭服务器


def main():
    ip = '192.168.1.135'

    telent_ssh('192.168.1.146', '22', 'kali', '314313')


if __name__ == '__main__':
    main()
