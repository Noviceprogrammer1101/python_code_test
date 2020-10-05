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


def is_palindrome(num):
    """
    判断一个数是不是回文数
    :param num: 正整数
    :return: 是回文数返回True，不是回文数返回False
    """
    #        请在此处添加代码       #
    # *************begin************#
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    # print(num, total)
    return total == num

    # **************end*************#


def is_prime(num):
    """
    判断一个数是不是素数
    :param num: 正整数
    :return: 是素数返回True，不是素数返回False
    """
    #        请在此处添加代码       #
    # *************begin************#
    flag=0
    for i in range(2,num):
        if num% i==0:
            flag=1
            break

    if flag==1:
        return False
    else:
        return True
    # **************end*************#



def prime_palindrome(num):
    """
        判断一个数是不是回文素数
        :param num: 正整数
        :return: 是回文素数返回True，不是回文素数返回False
        """
    #        请在此处添加代码       #
    # *************begin************#
    if(is_palindrome(num)==True) and (is_prime(num)==True):
        return True
    else:
        return False
    # **************end*************#


