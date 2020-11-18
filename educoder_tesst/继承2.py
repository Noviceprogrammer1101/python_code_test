class BankEmployee():
    def __init__(self, name="", num="", salary=3000):
        self.__name = name
        self.__num = num
        self.salary = salary

    def get_salary(self):  # 定义领工资方法get_salary()
        print("%s领到这个月工资%d" % (self.__name, self.salary))

    # 请在此处添加代码对name和num设置set/get方法 #
    # *************   begin   ************#
    def get_name(self):
        return self.__name

    def get_num(self):
        if self.__num.startswith('s'):
            return self.__num
        else:
            print('工号以s开头')
            return

    def set_name(self, name):
        self.__name = name

    def set_num(self, num):
        if num.startswith('s'):
            self.__num = num
        else:
            print('工号以s开头')
        self.__num = num
    # **************  end   *************#


class BankTeller(BankEmployee):
    #        请在此处添加代码         #
    # *************begin************#
    def __init__(self, name="", num="", salary=2000):
        super().__init__(name, num, salary)


# **************end*************#

def main():
    bankteller = BankTeller()
    name = input()
    num = input()
    bankteller.set_name(name)
    bankteller.set_num(num)
    bankteller.get_salary()
    print(bankteller.get_name(), bankteller.get_num())


if __name__ == "__main__":
    main()