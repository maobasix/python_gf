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


if __name__ == '__main__':
    host = []
    users = []
    password = []
    for t in host:
        for i in users:
            for n in password:
                if ssh_login(t, i, n):
                    exit()
