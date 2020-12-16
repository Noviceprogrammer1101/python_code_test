#使用深度优先遍历目录
from os import listdir
from os.path import join,isfile,isdir
def listDirWidthFirst(path):
    """
    广度遍历优先算法遍历目录

    :param director: 需遍历的路径
    :return:无返回值，直接输出
    """
# *************begin************#
    if not isdir(path) and not isfile(path):
        print(path+' is not a directory or does not exist.')
        return
    dirs=[path]
    while dirs:
        current=dirs.pop(0)
        for subPath in sorted(listdir(current)):
            path1=join(current,subPath)
            if isfile(path1):
                print(path1)
            elif isdir(path1):
                print(path1)
                dirs.append(path1)
# **************end*************#


#遍历当前目录下的test目录
path = input()
listDirWidthFirst(path)