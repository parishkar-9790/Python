import sqlite3
from employee import ESX
conn = sqlite3.connect('X:\Python\src\SQL\sqlLite\SL01\emp.db')
c = conn.cursor()
emp1=ESX('jane','van',606060)
emp2=ESX('hank ','pym',1260)
while True:
    x=input('Enter Choice 1.Create Table 2.Add employee 3.show employee--> ')
    if x=='1':
        try:
            c.execute("""CREATE TABLE employee(
                    first text,
                    last text,
                    pay integer
                )""")
        except Exception as e:
            print(e)
    elif x=='2':
        c.execute("INSERT INTO employee VALUES(?,?,?)",(emp1.first,emp1.last,emp1.pay))
        # c.execute("INSERT INTO employee VALUES(:first,:last,:pay)",{'first':emp1.first,'last':emp1.last,'pay':emp1.pay})
        # c.execute("INSERT INTO employee VALUES('{}','{}',{})".format(emp1.first,emp1.last,emp1.pay))
        conn.commit()
        print('inserted data into table')
    elif x=='3':
        c.execute("SELECT * FROM employee WHERE last='van'")
        conn.commit()
        print(c.fetchall())
    
    elif x=='4':
        break
    
conn.commit()

conn.close()
