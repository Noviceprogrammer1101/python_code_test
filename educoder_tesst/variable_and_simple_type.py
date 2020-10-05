"""
将华氏温度转换为摄氏温度
"""

#********请输入您的代码********#
#************begin************#
celsius=eval(input())
c=(celsius-32)/1.8
print("{:.1f}华氏度 = {:.1f}摄氏度".format(celsius,c))
#************end************#




"""
输入半径计算圆的周长和面积


"""
import math
pi = math.pi   #pi = 3.14159

#*******请输入您的代码********#
#***********begin************#
r=eval(input())
zhouchang=2*pi*r
mianji=pi*r**2
print("周长: {:.2f}".format(zhouchang))
print("面积: {:.2f}".format(mianji))

#***********end************#



"""
输入你的姓和名，输出首字母大写的姓名

"""
first_name = input()
last_name = input()

#*******请输入您的代码********#
#***********begin************#
print(first_name.capitalize()+" "+last_name.capitalize())
#***********end************#


"""
输入年份 如果是闰年输出True 否则输出False
"""

# 如果代码太长写成一行不便于阅读 可以使用\对代码进行折行
#**************begin**************#
year = int(input())
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print("True")   # 整百年能被400整除的是闰年
        else:
            print("False")
    else:
        print("True")       # 非整百年能被4整除的为闰年
else:
    print("False")

#**************end****************#
