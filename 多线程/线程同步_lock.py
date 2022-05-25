import threading

number = 0


def plus(lock, name):
    global number
    for i in range(1000000):
        lock.acquire()      # 锁定
        print(name)
        number += 1
        lock.release()      # 解锁


def main():
    global number
    lock = threading.Lock()     # 创建线程锁lock
    threads = []
    for i in range(2):
        t = threading.Thread(target=plus, args=(lock, "线程"+str(i)))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print(f"主线程结束后number={number}")


if __name__ == '__main__':
    main()
