# 使用深度优先遍历目录
from os import listdir
from os.path import join, isfile, isdir


def listDirDepthFirst(path):
    """
    深度遍历算法遍历目录

    :param director: 需遍历的路径
    :return:无返回值，直接输出
    """
    # *************begin************#
    for subpath in sorted(listdir(path)):
        path1 = join(path, subpath)
        if isfile(path1):
            print(path1)
        elif isdir(path1):
            print(path1)
            listDirDepthFirst(path1)


# **************end*************#


# 遍历当前目录下的test目录
listDirDepthFirst('./test')