import numpy as np
'''
将array依次执行以下操作
1.把列表中的元素升序排序。
2.删除列表中的最后一个元素。
3.把列表中第一个元素移动到列表尾部。
4.返回新列表。
'''
array = [85,96,2,5,3,566,0,91,5234,5555,89,62,34]
#*******请输入您的代码********#
#***********begin************#
array.sort()
array.pop()
array.append(array.pop(0))
print(array)
#***********end************#

#x为传入的列表，完成函数编写，使其返回列表中最大值和第二大的值

def max2(x):
    #        请在此处添加代码       #
    # *************begin************#
    m2=max(x)
    x.pop(x.index(m2))
    m1=max(x)
    # **************end*************#
    return m1,m2  #m1是第二大的值,m2是最大值


def is_leap_year(year):
    """
    判断指定的年份是不是闰年

    :param year: 年份
    :return: 闰年返回True平年返回False
    """
    #        请在此处添加代码       #
    # *************begin************#
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True  # 整百年能被400整除的是闰年
            else:
                return False
        else:
            return True  # 非整百年能被4整除的为闰年
    else:
        return False
        # **************end*************#


def which_day(year, month, date):
    """
    计算传入的日期是这一年的第几天

    :param year: 年
    :param month: 月
    :param date: 日
    :return: 第几天
    """
    #        请在此处添加代码       #
    # *************begin************#
    days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]]

    days = days_of_month[is_leap_year(year)]
    total = 0
    for index in range(month - 1):
        total += days[index]
    return total + date

    # **************end*************#

#打印杨辉三角
#（不需返回函数值，直接打印）
def prin(num):
    ''':param num: 杨辉三角行数'''

#        请在此处添加代码       #
# *************begin************#
    if num<=0:
        print([])
    else:
        a = [1]
        print(a[0],end='\t')
        print()
        for i in range(num-1):
            b = []
            b.append(1)
            for j in range(len(a)-1):
                b.append(a[j]+a[j+1])
            b.append(1)
            for n in range(len(b)):
                print(b[n],end='\t')
            a = b
            print()
# **************end*************#


