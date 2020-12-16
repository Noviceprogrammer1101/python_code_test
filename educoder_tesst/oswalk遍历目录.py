import os
def listDiroswalk(path):
    """
    使用os.walk遍历目录

    :param director: 需遍历的路径
    :return:无返回值，直接输出
    """
# *************begin************#
    if not os.path.isdir(path):
        print(path+' is not a directory or does not exist.')
        return
    list_dirs=os.walk(path)
    for root,dirs,files in list_dirs:
        for d in dirs:
            print(os.path.join(root,d))
        for f in files:
            print(os.path.join(root,f))
# **************end*************#


#遍历当前目录下的test目录
path = input()
listDiroswalk(path)