# Author : Parishkar Singh  Python 3.10  2022
# ...............................................................
# Database sqlite3
# ...............................................................

import sqlite3
from tabulate import tabulate
    
def insertData(cur):
    n=input("Enter id/name/qty/price of the product-> ")
    cur.execute('insert into products values(?,?,?,?)',(n.split('/')))
    
def priceIncrease(cur):
    cur.execute('update products set price=price*1.1 where price<50')
    
def deleteData(cur):
    n=int(input('Enter product id to delete-> '))
    cur.execute(f'delete from products where id={n};')
    
def showAll(cur):
    result=cur.execute('select * from products;')
    print(tabulate(result, headers=['id','name','qty','price']))
    
def displayLess(cur):
    result=cur.execute('select * from products where qty<40;')
    print(tabulate(result, headers=['id','name','qty','price']))
    
if __name__ == '__main__':
    conn=sqlite3.connect("X:\Python\src\Termworks\prod.db")
    cur=conn.cursor()
    cur.execute("create table if not exists products (id integer,name text,qty integer,price integer,primary key(id))")
    while(True):
        x=input("Enter choice 1.Insert 2.delete 3.priceIncrease 4.showAll 5.displayLess-> ")
        if x=='1':
            insertData(cur)
        elif x=='2':
            deleteData(cur)
        elif x=='3':
            priceIncrease(cur)
        elif x=='4':
            showAll(cur)
        elif x=='5':
            displayLess(cur)
        conn.commit()