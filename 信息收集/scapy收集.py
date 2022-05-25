from scapy.all import IP, ICMP, TCP, sr1

target_hosts = ['192.168.1.149']
online_hosts = []
open_ports = []
for ip in target_hosts:
    package = IP(dst=ip) / ICMP()
    reply = sr1(package)
    if reply == None:
        continue
    if reply['ICMP'].type == 0 and reply['ICMP'].code == 0:
        online_hosts.append(reply['IP'].src)
for ip in online_hosts:
    for port in range(1, 101):
        package = IP(dst=ip) / ICP(dport=port, flags="S")
        reply = sr1(package)
        if reply == None:
            continue
        if reply['TCP'].flags == "SA":
            open_ports.append(port)
        online_hosts[ip] = online_hosts

for ip in online_hosts:
    print(f"{ip}在线，开放端口为{online_hosts[ip]}")