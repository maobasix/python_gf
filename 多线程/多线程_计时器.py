import multiprocessing
import sys
import time


def print_time():
    while True:
        sys.stdout.write(f"\r{time.strftime('%H:%M:%S')}")
        time.sleep(1)


if __name__ == '__main__':
    p1 = multiprocessing.Process(target=print_time)
    p1.start()
