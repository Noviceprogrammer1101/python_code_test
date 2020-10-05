def countlevel():
    '''

       :return:最小阶梯数
       '''
    #        请在此处添加代码       #
    # *************begin************#
    x = 7
    i = 1
    flag = 0
    while i <= 100:
        if (x % 2 == 1) and (x % 3 == 2) and (x % 5 == 4) and (x % 6 == 5):
            flag = 1
            break
        else:
            x = 7 * (i + 1)  # 根据题意，x 一定是7 的整数倍，所以每次乘以7
        i += 1
    if flag == 1:
        return x
        # **************end*************#


print(countlevel())


def triangle(row):
    '''
       根据row值，打印三个三角形
       :row:三角形行数
       :return: 无返回值
       '''
    #        请在此处添加代码       #
    # *************begin************#
    for i in range(row):
        for j in range(0, i + 1):
            print("*", end="")

        print("")
    for i in range(row):
        for j in range(0, row - i - 1):
            print("", end=" ")
        for k in range(row - i - 1, row):
            print("*", end="")
        print("")
    for i in range(row):
        for j in range(0, row - i - 1):
            print(end=" ")
        for k in range(row - i, row + i + 1):
            print("*", end="")
        print("")

        # **************end*************#


row = int(input())
triangle(row)

from random import randrange, randint, sample
import random


def display(balls):
    """
    按照题目所要求格式输出列表中的双色球号码

    :param balls:双色球号码列表，如[9,12,16,20,30,33 3]
    :print:输出格式为09 12 16 20 30 33 | 03
    :return: 无返回值

    """
    #        请在此处添加代码       #
    # *************begin************#
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print('|', end=' ')
        print('%02d' % ball, end=' ')
    print()
    # **************end*************#


def random_select():
    """
    随机选择一组号码
    :return: 返回随机选择的这一组号码，如[9,12,16,20,30,33 3]
    """
    #        请在此处添加代码       #
    # *************begin************#
    red_balls = [x for x in range(1, 34)]
    selected_balls = []

    selected_balls = sample(red_balls, 6)
    selected_balls.sort()
    selected_balls.append(randint(1, 16))
    return selected_balls

    # **************end*************#


# n为注数
def main(n):
    for _ in range(n):
        display(random_select())


random.seed(3)
n = int(input())
if __name__ == '__main__':
    main(n)


