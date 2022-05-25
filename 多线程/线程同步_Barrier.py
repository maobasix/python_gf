import sys
import threading
import time


def check(name, lock, b_lock):
    lock.acquire()
    sys.stdout.write(f"{name}正在核酸检测\n")
    time.sleep(0.2)
    lock.release()
    b_lock.wait()       # 等待其他线程
    sys.stdout.write(f"{name}已经完成核酸检测了\n")


def back_classroom():
    sys.stdout.write("\n啊？？？？？刚才做的不是核酸检测？？？？？\n")


if __name__ == '__main__':
    lock = threading.BoundedSemaphore(5)  # 同时五个
    b_lock = threading.Barrier(100, action=back_classroom)
    threads = []
    for i in range(1, 101):
        t = threading.Thread(target=check, args=("同学" + str(i), lock, b_lock))
        threads.append(t)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print("所有人都完成核酸检测")
