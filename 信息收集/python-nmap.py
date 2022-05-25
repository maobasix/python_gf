'''import nmap


def api(ip, port, arg):
    port = port if len(port) > 0 else None
    s = nmap.PortScanner()  # 创建对象
    result = s.scan(hosts=ip, ports=port, arguments=arg)  # 扫描目标
    for n in s.all_hosts():
        print(f"\n{n}在线")
        print(f"操作系统版本为:{s[n]['osmatch'][0]['name']}")
        print("端口 名称 状态 版本 产品")
        for p in s[n].all_tcp():
            print(p, s[n]['tcp'][p]['name'], s[n]['tcp'][p]['state'], s[n]['tcp'][p]['version'],
                  s[n]['tcp'][p]['product'], sep=' ')
    return result


if __name__ == '__main__':
    ht = '192.168.1.149'  # 扫描的hosts
    pt = '1-500'  # 扫描的端口
    ag = '-sV -O'  # nmap的参数
    message = api(ht, pt, ag)
    # print(message)
'''

import nmap


def print_result(ip, scan_result):
    print(f"\n{ip}主机在线，其开放的tcp端口为：")
    if 'scan' in scan_result:  # 判断是否有扫描结果
        for ip in scan_result['scan'].keys():  # 其他ip地址
            if 'tcp' in scan_result['scan'][ip]:  # 判断是否有该ip主机tcp信息
                for port in scan_result['scan'][ip]['tcp'].keys():  # 提取tcp端口
                    print(port, end=' ')


def main():
    target_hosts = '192.168.1.149'
    target_porst = '1-500'
    nma = nmap.PortScannerAsync()
    nma.scan(hosts=target_hosts, ports=target_porst, arguments='-sS', callback=print_result)
    nma.wait()


if __name__ == '__main__':
    main()
