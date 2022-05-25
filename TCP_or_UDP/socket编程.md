socket编程

UDP编程

UDP实例

TCP编程

TCP实例

介绍

Socket(套接字)是计算机进行网络通信的一套程序接口

基于客户端/服务器结构（C/S）可以隐藏复杂的TCP/IP协议族，只要遵循Socket的规定就可以进行网络程序开发，，简单且开发效率高。

Python中的Socket模块，提供的套接字编程钉钉大部分功能支持使用UDP和TCP协议进行网络通信

UDP属于无连接协议，在向接收方发送消息时，不需要建立连接，而是直接发下哦那个即可。

UDP的应用：域名系统，视频流，ip语言

![img](file:///G:\QQ\3032147041\Image\C2C\26FCE46A0E49BE4ADE84BE3E1B1EDD35.jpg)



UDP编程

1.socket([family[,type[,proto]]]):创建Socket对象

![img](file:///G:\QQ\3032147041\Image\C2C\D4439109D498DC8CA89FA94E2304C0C9.jpg)

2.bind(address)：绑定地址元组（ip,端口）

3.sendto(string,address):发送数据

把string发送给指定的address

把其中address格式（ip，端口）

4.recvfrom(bufize[,flags])：接收数据

返回值时（data,address）.data为接收的字符串，address数数据发送方的套接字地址

![img](file:///G:\QQ\3032147041\Image\Group2\HR\DT\HRDT{B9%A6BQW5REX6ZPJ]A.png)