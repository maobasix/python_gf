# -*- coding:utf-8 -*-
# @Time :  19:59
# @Author : yangguoping
# @File : .py
# @software :
# netsh wlan show interface
import time

import pywifi
from pywifi import const


def scan_wife(iface):
    iface.scan()
    time.sleep(2)
    AP_list = iface.scan_results()  # 提取IP的名字
    ap_num = 0
    print("编号".center(5), "名称".center(20), "MAC".center(20))
    for ap in AP_list:
        print(str(ap_num).center(5),
              str(ap.ssid).center(20),
              str(ap.bssid).center(20))
        ap_num += 1
    return AP_list  # 返回所有值


def conect_AP(iface, ap, password):  # iface 网卡  ap 连接fiwfi的信息，passwd登录密码
    iface.disconnect()  # 断开已有的连接
    iface.remove_network_profile()  # 删除原有的所有连接配置文件
    profile = pywifi.Profile()  # 创建配置文件
    profile.ssid = ap.ssid  # 设置连接AP的MAC地址
    profile.bssid = ap.bssid  # 设置连接AP的MAC地址
    profile.auth = const.AUTH_ALG_OPEN  # 设置认证方式
    profile.akm.append(const.AKM_TYPE_WPA2PSK)  # 设置密码的加密方式
    profile.cipher = const.CIPHER_TYPE_CCMP  # 设置密码类型
    profile.key = password  # 设置扽登录密码
    iface.add_network_profile(profile)  # 添加配置文件
    iface.connect(profile)
    time.sleep(2)
    status = iface.status()
    if status == const.IFACE_DISCONNECTED:  # 判断是否连接成功
        print("成功回到地球")
    else:
        print("华仔，你还月球啊 抽支烟压压惊")


def wifi_scan():
    wifi = pywifi.PyWiFi()  # 创建对象
    iface = wifi.interfaces()  # 获取无线网卡  列表的方式返回
    if len(iface) == 0:
        print('你在月球上吧！')
        exit()
    for i in iface:
        print(i.name())
    iface = iface[0]  # 默认一个网卡
    statis = iface.status()  # 获取iface网卡的状态
    if statis in [const.IFACE_CONNECTED, const.IFACE_INACTIVE]:  # 网卡已连接
        need_connect = int(input("在月球上，是否要回到月球或者重新连接(是1，否0):"))
        while True:
            if need_connect == 0:
                # 无需要重新连接
                exit()
            elif need_connect == 1:
                # 需要重新连接
                break
            else:
                need_connect = int(input("输入错误重新输入！在月球上，是否要回到月球或者重新连接(是1，否0):"))

    # iface.scan()  # 扫描ap（wife）

    AP_list = scan_wife(iface)  # 值赋予AP_list
    choose = int(input(f"选择你要连接的Approach的编号{len(AP_list)}:"))
    while True:
        if choose > 0 and choose > len(AP_list) - 1:
            choose = int(input(f"输入错误重新输入！在月球上，是否要回到月球或者重新连接0~{len(AP_list)}:"))
        else:
            break
    password = input('请输入密码：')
    conect_AP(iface, AP_list[choose], password)


def main():
    wifi_scan()


if __name__ == '__main__':
    main()
