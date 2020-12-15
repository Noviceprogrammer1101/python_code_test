#
# from multiprocessing import Process
# import os
# def fun(name):
#     print('run child process%s(%s)'%(name,os.getpid()))
#     print('hello ',name)
#
# # 弄个多进程还得弄出一个main出来，不然报错
# if __name__=='__main__':
#     print('parent process%s'%os.getpid())
#     p=Process(target=fun,args=('zhang',))
#     print('child process start')
#     p.start()
#     p.join()
#     print('parent process finished')


# import multiprocessing
# import os
#
# class my(multiprocessing.Process):
#     def __init__(self,name):
#         self.name=name
#         super().__init__()
#
#     def run(self):
#         print('child process%s(%s)'%(self.name,os.getpid()))
#         print('hello ',self.name)
#
# if __name__=='__main__':
#     print('parent process%s'%os.getpid())
#     p=my('zhang')
#     print('child process start')
#     p.start()
#     p.join()
#     print('parent process finished')

# from multiprocessing import Pool
# import os,time,random
# def fun(num):
#     print('child process%s running(%s)'%(num,os.getpid()))
#     time.sleep(random.random()*3)
# if __name__=='__main__':
#     print('parent process%s'%os.getpid())
#     p=Pool(5)
#     for i in range(8):
#         p.apply_async(fun,args=(i,))
#         # p.apply(fun,args=(i,))
#     print('waiting for all child process finished')
#     p.close()
#     p.join()
#     print('all process  finished')

# import multiprocessing
# import os,time
# def fun(num):
#     mysum=0
#     for i in range(num):
#         print('(%s)processing is rnning:%d'%(os.getpid(),i))
#         mysum+=i
#     return mysum
#
# if __name__=='__main__':
#     with multiprocessing.Pool(4) as pool:
#         re=pool.map(fun,(3,6,9))
#         for item in re:
#             print(item)
from numpy import *
print(eye(4))