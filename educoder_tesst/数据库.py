import sqlite3
import os

def create(sql):
    '''建立表COMPANY'''
    conn = sqlite3.connect(sql)
    # print("open database successfully")
    c = conn.cursor()
    c.execute('''CREATE TABLE COMPANY
           (ID INT PRIMARY KEY     NOT NULL,
          NAME           TEXT    NOT NULL,
           AGE            INT     NOT NULL,
           ADDRESS        CHAR(50),
           SALARY         REAL);''')
    # print("Table created successful")
    conn.commit()
    conn.close()
def select(sql):
    """
    输出数据库中的内容
    :param sql: 数据库（如test.db）
    :return:
    """
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    cursor = c.execute("SELECT id, name, address, salary  from COMPANY")
    for row in cursor:
        print("ID = ", row[0])
        print("NAME = ", row[1])
        print("ADDRESS = ", row[2])
        print("SALARY = ", row[3])
        print("\n")
    conn.close()
def insert(sql):
    '''
    往数据库中插入（增加）如下数据
    ID, NAME,   AGE,     ADDRESS,    SALARY
    1, 'Paul',  32,   'California', 20000.00
    2, 'Allen', 25,      'Texas',   15000.00
    3, 'Teddy', 23,      'Norway',  20000.00
    4, 'Mark',  25,    'Rich-Mond', 65000.00

    :param sql:数据库（如test.db）
    :return:无返回
    '''
    #        请在此处添加代码       #
    # *************begin************#
    conn = sqlite3.connect(sql)
    c = conn.cursor()
    c.execute('''insert into COMPANY values (1,'Paul',32,'California', 20000.00),(2, 'Allen', 25,'Texas',15000.00),(3,'Teddy',23,'Norway',20000.00),(4,'Mark',25,'Rich-Mond', 65000.00)''')
    conn.commit()
    conn.close()
    # **************end*************#

def update(sql):
    '''
    更新数据库中的数据
    将ID=1的SALARY更新为25000.00

    :param sql:数据库（如test.db）
    :return:无返回
    '''
    #        请在此处添加代码       #
    # *************begin************#
    conn = sqlite3.connect(sql)
    c = conn.cursor()
    c.execute('update COMPANY set SALARY=25000.00 where ID=1')
    conn.commit()
    conn.close()
    # **************end*************#

def delete(sql):
    '''
    删除数据库中的数据
    将ID=2的数据删除
    :param sql: 数据库（如test.db）
    :return: 无返回
    '''
    #        请在此处添加代码       #
    # *************begin************#
    conn = sqlite3.connect(sql)
    c = conn.cursor()
    c.execute('delete from COMPANY where ID=2')
    conn.commit()
    conn.close()
    # **************end*************#

if __name__ == '__main__':
    #create('test.db')
    #insert('test.db')
    update('test.db')
    delete('test.db')
    select('test.db')
    os.remove('test.db')