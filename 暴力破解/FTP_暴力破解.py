import ftplib

target = '127.0.0.1'
user = 'admin'
passwd = '123456'
ftp = ftplib.FTP()
reply = ftp.connect(host=target, port=21)
if '220' in reply:
    reply = ftp.login(user, passwd)
    if '230' in reply:
        print("ok")
    else:
        print("no")
else:
    print("链接失败")
