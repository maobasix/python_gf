# -*- coding:utf-8 -*-
# @Time :  19:59
# @Author : yangguoping
# @File : .py
# @software :
# netsh wlan show interface
import time

import pywifi
from  pywifi import const

def scan_wife(iface):

    iface.scan()
    time.sleep(2)
    AP_list=iface.scan_results() # 提取IP的名字
    ap_num=0
    print("编号".center(5),"名称".center(20),"MAC".center(20))
    for ap in AP_list:
        print(str(ap_num).center(5),
              str(ap.ssid).center(20),
              str(ap.bssid).center(20))
        ap_num+=1

def wifi_scan():
    wifi=pywifi.PyWiFi()  # 创建对象
    iface=wifi.interfaces() # 获取无线网卡  列表的方式返回
    if len(iface)==0:
        print('你在月球上吧！')
        exit()
    for i in iface:
        print(i.name())
    iface=iface[0]  #默认一个网卡
    statis= iface.status() # 获取iface网卡的状态
    if statis in [const.IFACE_CONNECTED,const.IFACE_INACTIVE]: #网卡已连接
        need_connect=int(input("在月球上，是否要回到月球或者重新连接(是1，否0):"))
        while True:
            if need_connect==0:
                #无需要重新连接
                exit()
            elif need_connect==1:
                #需要重新连接
                break
            else:
                need_connect=int(input("输入错误重新输入！在月球上，是否要回到月球或者重新连接(是1，否0):"))

    # iface.scan()  # 扫描ap（wife）
    scan_wife(iface)



def main():
    wifi_scan()

if __name__ == '__main__':
    main()