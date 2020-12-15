import threading
from random import randint
from time import sleep


class Account():

    def __init__(self, account, money):
        self.account = account
        self.money = int(money)
        self.flags = False


def get_monney(Class, name, account, money):
    while True:
        sleep(randint(2, 3))
        con.acquire()
        if (Class.money > 100 and Class.flags == True):
            me = randint(100,Class.money)
            Class.money -= me
            Class.flags = False
            print(name + "为账户" + Class.account + "取钱 "+str(me)+"元 ，余额为 %d 元" % Class.money)
            con.notify()
        else:
            con.wait()
        con.release()


def put_monney(Class, name, account, money):
    while True:
        sleep(randint(2, 3))
        con.acquire()
        Class.name = name
        if  Class.flags == True:
            con.wait()
        else:
            me = randint(200,1000)
            Class.money += me
            Class.flags = True
            print(Class.name + "为账户" + Class.account + "存钱 "+str(me)+"元 ，余额为 %d 元" % Class.money)

            con.notify()
        con.release()


con = threading.Condition()
A = Account('123', '200')

t1 = threading.Thread(name="A", target=get_monney, args=(A, 'A', '123', '200'))
t1.start()
t2 = threading.Thread(name="B", target=put_monney, args=(A, 'B', '123', '200'))
t2.start()