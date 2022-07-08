# Author : Parishkar Singh  Python 3.10  2022
# ...............................................................
# Termwork 3
# ...............................................................
import csv
from tabulate import tabulate

if __name__ == '__main__':
    with open('X:\\Python\\src\\Termworks\\Books.csv') as f:
        rs = csv.reader(f)
        header = list(next(rs))
        record= list(rs)
        while True:
            tempbooks=[]
            x=input('\n(partial name of author/books is acccepted also case insensitive! )\nEnter The Choice\n1.Search By Author\n2.Books Below Specified Price\n3.Search Books \n4.Show all books\n-->')
            if x=='1':
                temp=input('Enter the name of author -> ')
                tempbooks.clear()
                for i in record:
                    if temp.lower() in i[2].lower():
                        tempbooks.append(i)
                print('\nAvailable Books by the author are-->\n\n',tabulate(tempbooks, headers=header), end='\n\n')
            elif x=='2':
                temp=int(input('Enter the price to find books under it -> '))
                try:
                    if temp<=0:
                        raise Exception('price cant be free or negative')
                    tempbooks.clear()
                    for i in record:
                        if int(i[3])<=temp:
                            tempbooks.append(i)
                    print(f'\nAvailable Books under {temp} are-->\n\n',tabulate(tempbooks, headers=header), end='\n\n')
                except Exception as r:
                    print(r)
            elif x=='3':
                tempbooks.clear()
                temp=input('Enter the name of the book-> ')
                for i in record:
                    if temp.lower() in i[1].lower():
                        tempbooks.append(i)
                print(f'\nAvailable Books  are-->\n\n',tabulate(tempbooks, headers=header), end='\n\n')
            elif x=='4':
                print('\nAvailable Books are-->\n\n',tabulate(record, headers=header), end='\n\n')
            elif x=='5':
                f.close()
                break