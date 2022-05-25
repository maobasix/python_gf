import sys
import threading
import time

produce_num = 0


def producer(c_lock):
    global produce_num
    while True:
        c_lock.acquire()
        if produce_num == 10:
            c_lock.wait()

        sys.stdout.write("\n正在生产商品\n")

        while produce_num < 10:
            produce_num += 1
            sys.stdout.write(f"{produce_num}")
            time.sleep(0.8)

        c_lock.notify()
        c_lock.release()


def consumer(c_lock):
    global produce_num
    while True:
        c_lock.acquire()
        if produce_num == 0:
            c_lock.wait()

        sys.stdout.write("\n正在取出商品\n")

        while produce_num > 0:
            sys.stdout.write(f"{produce_num}")
            produce_num -= 1
            time.sleep(0.4)

        c_lock.notify()
        c_lock.release()


if __name__ == '__main__':
    c_lock = threading.Condition()
    t1 = threading.Thread(target=producer, args=(c_lock,))
    t1.start()
    t2 = threading.Thread(target=consumer, args=(c_lock,))
    t2.start()