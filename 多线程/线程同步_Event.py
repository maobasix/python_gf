import sys
import threading
import time


def signal_lamp(event):
    while True:
        sys.stdout.write("绿灯：\n")
        event.set()
        time.sleep(7)
        sys.stdout.write("红灯：\n")
        event.clear()
        time.sleep(5)


def car_go(car_name, event):
    if not event.is_set():
        sys.stdout.write(f"{car_name}等待绿灯\n")
        event.wait()

    sys.stdout.write(f"{car_name}正在通过\n")
    time.sleep(2)


def main():
    lock = threading.Event()
    thread1 = threading.Thread(target=signal_lamp, args=(lock,))
    thread1.start()
    cars = ["五菱宏光", "天子驾二", "九手奥拓", "猎鹿犬步战车", "99A主战坦克"]
    num = 0
    while True:
        for car in cars:
            t = threading.Thread(target=car_go, args=(car + str(num + 1), lock))
            t.start()
            num += 1


if __name__ == '__main__':
    main()
