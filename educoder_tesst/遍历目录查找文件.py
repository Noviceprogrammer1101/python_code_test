
from os import listdir
from os.path import join,isfile,isdir
def findfile(path,dstfile):
    """
    遍历目录中是否存在dstfile文件，如果存在输出该文件的内容，否则输出 dstfile does not exist.

    :param path: 需遍历的路径
    :dstfile: 需要查找的文件
    """
# *************begin************#
    if not isdir(path):
        print(path+' is not a directory or does not exist.')
    else:
        dirs=[path]
        a=0
        while dirs:
            current=dirs.pop(0)
            for sp in sorted(listdir(current)):
                path2=join(current,sp)
                if isfile(path2):
                    if sp==dstfile:
                        fp=open(path2,'r')
                        print(fp.read())
                        fp.close()
                        a=1
                elif isdir(path2):
                    dirs.append(path2)
        if(a==0):
            print(dstfile+' does not exist.')
# **************end*************#


#遍历当前目录下的test目录
path = input()
file = input()
findfile(path,file)