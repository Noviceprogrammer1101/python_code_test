class BankEmployee():
 #        请在此处添加代码         #
 # *************begin************#
    def __init__(self,name,num,salary=3000):
        self.__name=name
        self.__num=num
        self.salary=salary
    def get_salary(self):
        print('%s领到这个月工资%d'%(self.__name,self.salary))
 # **************end*************#

def main():
    name = input()
    num = input()
    bankemployee = BankEmployee(name,num)
    bankemployee.get_salary()

if __name__=="__main__":
    main()