import sys
import threading
import time


def check(name, lock):
    lock.acquire()
    sys.stdout.write(f"{name}正在核酸检测\n")
    time.sleep(2)
    lock.release()


if __name__ == '__main__':
    lock = threading.BoundedSemaphore(5)  # 同时五个
    threads = []
    for i in range(1, 101):
        t = threading.Thread(target=check, args=("同学" + str(i), lock))
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print("所有人都完成核酸检测")
