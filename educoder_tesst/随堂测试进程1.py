import multiprocessing
import math

# 使用进程池统计指定范围内的素数个数
def is_prime(m):
    """
    判断一个数m是不是素数
    :param m: 正整数
    """
    #        请在此处添加代码       #
    # *************begin************#
    if m < 2:
        return False
    if m == 2:
        return True
    if m % 2 == 0:
        return False
    sqrt_m = int(math.floor(math.sqrt(m)))
    for i in range(3, sqrt_m + 1, 2):
        if m % i == 0:
            return False
    return True
    # **************end*************#


def main(n):
    """
    判断0~n之间素数的个数
    :param m: 正整数
    """
    #        请在此处添加代码       #
    # *************begin************#
    with multiprocessing.Pool(4) as pool:
        print(sum(pool.map(is_prime, range(n))))
    # **************end*************#


if __name__ == '__main__':
    n = int(input())
    main(n)