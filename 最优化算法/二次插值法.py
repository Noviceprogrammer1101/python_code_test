'''
二次插值法python实现
f(x)=3*x^3-4*x-2极小值
区间[-1,6] e=0.05
'''
import numpy as np
import matplotlib.pyplot as plt
from time import sleep
from threading import Thread

'''
函数表达式
'''


# 返回3*x^3-4*x-2的函数值
def f(x):

    return 3 * pow(x, 3) - 4 * x + 2


# 定义变量们
X2, Y = list(), list()
k = 0
a = -2.5  # 左点
b = -0.3  # 右点
e = 0.001  # 精度
'''
绘制函数图像
'''


def close(time=1):
    sleep(time)
    # plt.savefig('./img/'+name)
    plt.close()
    pass


def printFunc():
    t = np.arange(a, b, 0.01)
    s = f(t)
    plt.plot(t, s)


def update_point(x, y):
    global k
    printFunc()

    plt.plot(x, y, 'ro')
    plt.text(x[-1], y[-1], k, color='red', fontsize=k + 10)
    # else:
    #     plt.plot([x], [y], 'ro')
    #     plt.text(x, y, k, color='red', fontsize=k + 10)
    thread1 = Thread(target=close, args=())
    thread1.start()
    # print('打开')
    plt.show()
    # print("close")


def final_fun(x, y):
    global k
    printFunc()
    plt.plot(x, y, 'ro')
    for i in range(1, k + 1):
        plt.text(x[i - 1], y[i - 1], i, color='red', fontsize=i + 10)
    # thread1 = Thread(target=close, args=())
    # thread1.start()
    plt.show()


'''
e为精度
'''


def search(f, x1, x2, x3):
    global k
    k += 1
    if f(x2) > f(x1) or f(x2) > f(x3):
        print("不满足两头大中间小的性质")
        return 0

    # 系数矩阵
    A = [[pow(x1, 2), x1, 1], [pow(x2, 2), x2, 1], [pow(x3, 2), x3, 1]]
    b = [f(x1), f(x2), f(x3)]

    X = np.linalg.solve(A, b)

    a0, a1, _ = X

    x = - a1 / (2 * a0)

    # 达到精度退出
    if abs(x - x2) < e:
        if f(x) < f(x2):
            y = f(x)
            print('最后的x:', x)
            X2.append(x)
            Y.append(y)
            final_fun(X2, Y)
            return (X2, Y)
        else:
            y = f(x2)
            print("最后的x2", x2)
            X2.append(x2)
            Y.append(y)
            final_fun(X2, Y)
            return (X2, Y)
    arr = [x1, x2, x3, x]
    arr.sort()
    # 在x2和新算出的x中找最小值
    if f(x2) > f(x):
        index = arr.index(x)
        x2 = x
    else:
        index = arr.index(x2)

    x1 = arr[index - 1]
    x3 = arr[index + 1]
    X2.append(x2)
    Y.append(f(x2))
    print('运行中的第%d次：%f' % (k, x2))
    update_point(X2, Y)

    return search(f, x1, x2, x3)


def regre(f, a, b):
    x1 = a
    x3 = b
    x2 = (a + b) / 2.0
    search(f, x1, x2, x3)


regre(f, a, b)