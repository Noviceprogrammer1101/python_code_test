#统计大写字母出现的次数，并按照字母出现次数降序排序输出
def countchar(file):
# *************begin************#
    fp=open(file,'r')
    ch=fp.read()
    adict={}
    for i in ch:
        if i.isalpha():
            if i.isupper():
                if i in adict:
                    adict[i]+=1
                else:
                    adict[i]=1
    for x in sorted(adict.items(),key=lambda e:e[1],reverse=True):
        print(x)
    fp.close() #关闭文件

# **************end*************#


file = input()
countchar(file)