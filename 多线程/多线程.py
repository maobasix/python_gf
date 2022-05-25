import threading
import time


def loop1(s, s2):
    time.sleep(s)
    print("loop1正在运行，已经延迟%s秒" % s)
    time.sleep(s2)
    print("loop1正在运行，已经延迟%s秒" % s2)


def loop2(s):
    print("loop2正在运行，已经延迟0秒")
    time.sleep(s)
    print("loop2正在运行，已经延迟%s秒" % s)


t = threading.Thread(target=loop1, args=(0, 1), name='loop1')
t2 = threading.Thread(target=loop2, args=(2,), name='loop2')

t.start()
t2.start()

