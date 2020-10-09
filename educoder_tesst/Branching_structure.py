"""
英制单位英寸和公制单位厘米互换
"""


def cmin(value, unit):
    ''':param value:长度，
        :param unit:单位'''

    #        请在此处添加代码       #
    # *************begin************#
    if (unit == "cm" or unit == "厘米"):
        i = value / 2.54
        print("{:.2f}英寸".format(i))
    elif (unit == "in" or unit == "英寸"):
        c = value * 2.54
        print("{:.2f}厘米".format(c))
    else:
        print('请输入有效的单位')
        # **************end*************#

# 这是cmin的此时函数，运行它可以得出结果
"""
value = input()
value = int(value)
unit = input()
cmin(value, unit)

"""



def invert(score):
    '''
    百分制成绩转换为等级制成绩
    :param score:百分制分数
    :return: 等级（A，B，C，D，E）
    '''
    #        请在此处添加代码       #
    # *************begin************#
    if (90 <= score <= 100):
        print('A')
    elif (80 <= score < 90):
        print('B')
    elif (70 <= score < 80):
        print('C')
    elif (70 <= score < 80):
        print('D')
    else:
        print('E')
        # **************end*************#

# 这是invert的测试函数
"""
score = float(input())
grad = invert(score)

"""

# print(grad)


'''《幸运的基督徒》
有15个基督徒和15个非基督徒在海上遇险，
为了能让一部分人活下来不得不将其中15个人扔到海里面去，
有个人想了个办法就是大家围成一个圈，由某个人开始从1报数，
报到9的人就扔到海里面，他后面的人接着从1开始报数，
报到9的人继续扔到海里面，直到扔掉15个人。由于上帝的保佑，
15个基督徒都幸免于难，问这些人最开
始是怎么站的，哪些位置是基督徒哪些位置是非基督徒。
'''

def main():
    #        请在此处添加代码       #
    # *************begin************#
    #person中存储30个true
    persons = [True] * 30
    counter, index, number = 0, 0, 0
    while counter < 15:
        if persons[index]:
            number += 1
            if number == 9:  #报到9数字的人就是false,淘汰掉
                persons[index] = False
                counter += 1   #记录淘汰的人数
                number = 0   #重新再报数
        index += 1 #向前一人
        index %= 30  #一直在30当中运行
    # 输出30个人的状态，可以看那些人在，那些人不在了
    for person in persons:
        print('1' if person else '0', end='')
    # **************end*************#


if __name__ == '__main__':
    main()