import queue
import sys
import threading
import time


def producer(queue1):
    produce_num = 5
    while True:
        produce_num += 1
        queue1.put(f"存入商品{produce_num}")  # 队列中存数据
        time.sleep(0.5)


def consumer(queue1):
    while True:
        produce = queue1.get()  # 从队列中取数据
        print(type(produce))
        sys.stdout.write(f"{produce}\n")
        time.sleep(0.3)


if __name__ == '__main__':
    queue1 = queue.Queue(10)
    t1 = threading.Thread(target=producer, args=(queue1,))
    t1.start()

    t2 = threading.Thread(target=consumer, args=(queue1,))
    t2.start()
