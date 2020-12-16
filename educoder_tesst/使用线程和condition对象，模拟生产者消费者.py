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



#另一个版本

import threading,time
class Producer(threading.Thread):
    def __init__(self,threadname):

        threading.Thread.__init__(self,name=threadname)

    def run(self):
        global count
        while True:
            if con.acquire():
                if count>100:
                    con.wait()

                else:
                    count=count+50
                    print(self.name+' produce 50,count='+str(count))
                    con.notify()

                con.release()

class Consumer(threading.Thread):
    def __init__(self,threadingname):
        threading.Thread.__init__(self,name=threadname)
    def run(self):
        global count
        while True:
            if count<100:
                con.wait()

            else:
                count=count-25
                print(self.name+' counsumer 25,count='+str(count))
                con.notify()
            con.release()
            time.sleep(1)

count=200
con=threading.Condition()
def test():
    for i in range(2):
        p=Producer('producer')
        p.start()
    for i in range(3):
        c=Consumer('consumer')
        c.start()

if __name__=='__main__':
    test()