# 反转一个只有三位数的整数

class Solution:
    # 参数number:一个三位数的整数
    # 返回值：反转后的数字
    def reverseinteger(self,number):
        h=int(number/100)
        t=int(number%100/10)
        z=(number%10)

        return 100 * z+ 10 * t + h
# 主函数
if __name__=='__main__':
    solution=Solution()
    num=int(input("please input a integer number: "))
    ans=solution.reverseinteger(num)
    print('input: ',num)
    print('output: ',ans)