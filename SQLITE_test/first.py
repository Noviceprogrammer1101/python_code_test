import sqlite3
conn=sqlite3.connect('example.db')
c=conn.cursor()

#c.execute('''create table stocks(date text,trans text,symbol text,qty real,price real)''')
#c.execute("insert into stocks values('2006-02-01','buy','rhat',100,35.14)")

#
for row in c.execute('select * from stocks ORDER by price'):
    print(row)
conn.commit()
conn.close()