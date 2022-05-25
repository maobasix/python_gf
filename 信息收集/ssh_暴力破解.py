import paramiko


def ssh_login(target, user, passwd):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(target, 22, user, passwd)
        print("login成功")
        return True
    except:
        return False


def massge(puth, puth1):
    with open(puth, 'r') as f:
        users.append(f)
    with open(puth1, 'r') as f1:
        password.append(f1)


if __name__ == '__main__':
    host = []
    users = []
    password = []
    massge('user.txt', 'password.txt')
    for t in host:
        for i in users:
            for n in password:
                if ssh_login(t, i, n):
                    exit()
