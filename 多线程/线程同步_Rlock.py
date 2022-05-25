import threading


def inner(lock1):
    lock1.acquire()     # 加锁
    # with lock1:
    print(f"inner1 function:{threading.current_thread()}")
    lock1.release()     # 解锁


def outer(lock1):
    print(f"outer function:{threading.current_thread()}")
    with lock1:     # 自动解锁
        inner(lock1)


def main():
    lock1 = threading.Lock()
    t1 = threading.Thread(target=outer, args=(lock1,))
    t2 = threading.Thread(target=outer, args=(lock1,))
    t1.start()
    t2.start()


if __name__ == "__main__":
    main()
