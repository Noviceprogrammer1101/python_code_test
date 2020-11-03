from math import sqrt


class Point(object):

    def __init__(self, x=0, y=0):
        """初始化方法

        :param x: 横坐标
        :param y: 纵坐标
        """
        self.x = x
        self.y = y

    def move_to(self, x, y):
        """移动到指定位置

        :param x: 新的横坐标
        "param y: 新的纵坐标
        :return : 无返回值
        """
        #        请在此处添加代码       #
        # *************begin************#
        self.x=x
        self.y=y
        # **************end*************#

    def move_by(self, dx, dy):
        """移动指定的增量

        :param dx: 横坐标的增量
        "param dy: 纵坐标的增量
        :return : 无返回值
        """
        #        请在此处添加代码       #
        # *************begin************#
        self.x+=dx
        self.y+=dy
        # **************end*************#

    def distance_to(self, other):
        """计算与另一个点的距离

        :param other: 另一个点,坐标为(other.x,other.y)
        ：return ：返回两点之间的距离
        """
        #        请在此处添加代码       #
        # *************begin************#
        return sqrt((other.x-self.x)**2+(other.y-self.y)**2)
        # **************end*************#

    def __str__(self):
        return '(%s, %s)' % (str(self.x), str(self.y))

x1,y1 = input().split(',')
x2,y2  = input().split(',')
x1 = int(x1)
y1 = int(y1)
x2 = int(x2)
y2 = int(y2)
dx,dy = input().split(',')
dx = int(dx)
dy = int(dy)

p1 = Point(x1, y1)
p2 = Point(x2,y2)
print('p1点的坐标为：',p1)
print('p2点的坐标为：',p2)

p2.move_by(dx, dy)
print('移动后的坐标为：',p2)
print('p1与p2点的距离为：',p1.distance_to(p2))