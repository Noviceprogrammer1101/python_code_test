
#题目
#求f(x)=100((x2-x1^2)^2)+(1-x1)^2，在xk=(0,0)^T,沿方向pk(1,0)^T的近似步长为alpha
from numpy import *
import sys


# MAXINT为无穷大
MAXINT=sys.maxsize

# 返回偏导的函数矩阵
def gradient_(X):
    x1=X[0]
    x2=X[1]
    return array([(-400*(x2-x1**2)**2*x1-2*(1-x1)),200*(x2-x1**2)])
# 返回原函数的函数值
def f(X):
    x1=X[0]
    x2=X[1]
    return 100*(x2-x1**2)**2+(1-x1)**2
if "__main__":
    '''
    Xk:point
    Pk:direction
    '''
    # 初始化
    Xk=array([0,0])
    Pk=array([1,0])

    mu_=0.1
    sigma=0.5
    Fk=f(Xk)
    Gk=gradient_(Xk)
    print('Gk=%s^T,Fk=%s,Gk^T*PK=%s'%(Gk,Fk,sum(gradient_(Xk)*Pk)))

    alpha=1

    b=MAXINT
    a=0
    j=0

    flag=1
    # i为循环变量
    i=0
    # 开始进行运算
    while(flag):
        Xk1=Xk+alpha*Pk
        Fk1=f(Xk1)

        print('第%s此迭代，alpha=%s,Xk1=%s,Fk1=%s'%(i,alpha,Xk1,Fk1))
        if Fk-Fk1 < -(mu_*alpha*sum(gradient_(Xk)*Pk)):

            b=alpha
            alpha=(alpha+a)*0.5

            i=i+1
        # 否则停止
        else:
            flag=0
    Xk1 = Xk + alpha * Pk
    Fk1 = f(Xk1)
    print (alpha,Fk1,Xk1)

