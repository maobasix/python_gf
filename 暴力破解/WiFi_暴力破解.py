import pywifi
from pywifi import const


def ap():
    wifi = pywifi.PyWiFi()  # 创建wifi对象
    iface = wifi.interfaces()  # 以列表方式返回所有网卡
    if len(iface):
        for i in iface:
            print(i)
    else:
        print("没有网卡")


if __name__ == '__main__':
    ap()
