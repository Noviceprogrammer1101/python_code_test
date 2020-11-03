#打印杨辉三角
#（不需返回函数值，直接打印）
def prin(num):
    ''':param num: 杨辉三角行数'''
# 1800301532韦柳栌
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


num = input()
num = int(num)
prin(num)