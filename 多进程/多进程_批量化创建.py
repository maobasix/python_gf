"""import multiprocessing
import sys
import time


def print_info(num):
    sys.stdout.write(f"进程{num}开始执行...\n")
    time.sleep(2)
    sys.stdout.write(f"进程{num}结束执行...\n")


if __name__ == '__main__':
    pool = multiprocessing.Pool(5)  # 创建进程池，并指定大小
    for i in range(2):
        pool.apply_async(func=print_info, args=(i,))        # async 表示异步，不添加则是同步

    pool.close()
    pool.join()

    sys.stdout.write("所有进程执行完毕\n")
"""

import multiprocessing
import sys
import time


# def print_info(num):
#     sys.stdout.write(f"进程{num}开始执行...\n")
#     time.sleep(2)
#     sys.stdout.write(f"进程{num}结束执行...\n")
#
# def main():
#     pool = multiprocessing.Pool(2)  #创建进程池，并指定其大小
#
#
#     for i in range(1,3):        #创建子进程
#         pool.apply_async(func=print_info,args=(i,))
#
#
#     #关闭进程池
#     pool.close()
#     pool.join()         #等待进程池中的进程运行结束
#
#     sys.stdout.write("所有进程都已经执行完毕！\n")
#
#
# if __name__ == '__main__':
#     main()

# 判断1000以内的数是否为素数，并统计素数的个数。

def is_prime(num):  # 判断num是否为素数
    if num < 2:  # 不是素数
        return 0
    if num == 2:
        sys.stdout.write(f"{num}\n")
        return 1
    if not num & 1:  # 如果为偶数则不是素数
        return 0

    # 大于等于2的奇数的判断
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:  # 能够被该范围内的数整除，则不是素数
            return 0
    # 如果为素数，先输出素数本身，再返回1
    sys.stdout.write(f"{num}\n")
    return 1


def main():
    pool = multiprocessing.Pool(5)

    totle = sum(pool.map(is_prime, range(1, 1001)))

    pool.close()
    pool.join()
    sys.stdout.write(f"素数的个数为：{totle}\n")


if __name__ == '__main__':
    main()
