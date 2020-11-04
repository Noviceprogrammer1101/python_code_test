"""
某公司有三种类型的员工 分别是部门经理、程序员和销售员
需要设计一个工资结算系统 根据提供的员工信息来计算月薪
部门经理的月薪是每月固定15000元
程序员的月薪按本月工作时间计算 每小时150元
销售员的月薪是1200元的底薪加上销售额5%的提成
"""
from abc import ABCMeta, abstractmethod


class Employee(object, metaclass=ABCMeta):
    """员工"""

    def __init__(self, name):
        """
        初始化方法

        :param name: 姓名
        """
        #        请在此处添加代码       #
        # *************begin************#
        self._name = name



        # **************end*************#

    @property
    def name(self):
        '''返回姓名'''
        #        请在此处添加代码       #
        # *************begin************#
        return self._name
        # **************end*************#

    @abstractmethod
    def get_salary(self):
        """
        获得月薪

        :return: 月薪
        """
        pass

# 继承了Employee类
class Manager(Employee):
    """部门经理"""

    def get_salary(self):
        return 15000.0


class Programmer(Employee):
    """程序员"""

    def __init__(self, name, working_hour=0):
        """
              初始化方法

              :param name: 姓名
              :param working_hour：工作时长

              """
        #        请在此处添加代码       #
        # *************begin************#
        # //调用父类的方法
        super().__init__(name)

        # self.__name = name
        self._working_hour = working_hour
        # **************end*************#

    @property
    def working_hour(self):
        '''返回工作时长'''
        #        请在此处添加代码       #
        # *************begin************#
        return self._working_hour
        # **************end*************#

    @working_hour.setter
    def working_hour(self, working_hour):
        '''
        设置工作时长
        :param working_hour:工作时长
        '''
        #        请在此处添加代码       #
        # *************begin************#
        self._working_hour = working_hour
        # **************end*************#

    def get_salary(self):
        '''返回程序员所得工资'''
        #        请在此处添加代码       #
        # *************begin************#
        return self._working_hour*150.0
        # **************end*************#


class Salesman(Employee):
    """销售员"""

    def __init__(self, name, sales=0):
        """
                   初始化方法

                   :param name: 姓名
                   :param sales：销售额

                   """
        #        请在此处添加代码       #
        # *************begin************#
        super().__init__(name)
        self._sales=sales
        # **************end*************#
    @property
    def sales(self):
    #        请在此处添加代码       #
    # *************begin************#
        return self._sales
    # **************end*************#


    @sales.setter
    def sales(self, sales):
    #        请在此处添加代码       #
    # *************begin************#
        self._sales=sales
    # **************end*************#


    def get_salary(self):

    #        请在此处添加代码       #
    # *************begin************#
        return 1200 + self._sales * 0.05
    # **************end*************#

# from salay import *
# from abc import ABCMeta, abstractmethod


def main():
    emps = [
        Manager('刘备'), Programmer('诸葛亮'),
        Manager('曹操'), Salesman('荀彧'),
        Salesman('吕布'), Programmer('张辽'),
        Programmer('赵云')
    ]
    for emp in emps:
        if isinstance(emp, Programmer):
            emp.working_hour = 7
        elif isinstance(emp, Salesman):
            emp.sales = 100
        # 同样是接收get_salary这个消息但是不同的员工表现出了不同的行为(多态)
        print('%s本月工资为: ￥%s元' %
              (emp.name, emp.get_salary()))


if __name__ == '__main__':
    main()

