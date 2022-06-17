import csv
from tabulate import tabulate
import matplotlib.pyplot as plt
from operator import itemgetter


if __name__ == '__main__':
    with open("X:\\Python\\src\\Assignments\\4_16June\\supermarket.csv") as f:
        rs = csv.reader(f)
        header = next(rs)
        record = list(rs)
        # the array of dict objects
        array = [{x[0]:x} for x in record]
        # print(list(array[1].values()))
        # list = list(array[1].items()
        # print(list)
        newlist = sorted(array, key=lambda x: (
            len(list(x.values())[0][9]), list(x.values())[0][9]))
        # for i in array:
        #     for key, value in i.items():
        #         print(key, value[9])
        for i in newlist:
            for key, value in i.items():
                print(key, value[9])

        # while True:
        #     x = input("\nEnter Choice\n1.Maximum Spent\n2.Count Customers(Payment method:- Wallet, Cash, Credit Card)\n3.Female Customers (Brought More than 5 items and spent>200)")
        #     if x == '1':
        # newlist = list(record)
        # 9 is the index of the total buying cost
        # record.append(mult)
        # array.sort(key=lambda x: (len(x[9]), x[9]))
        # print(sorted(array,key=lambda x:x[])[-1])
        # record.sort(key=int)
        # sorted(record,key=lambda x: x[9])
        # print(newlist[])
        # print(record[0][9])
        # print(sorted(record,key=lambda x:x[9]))
        # print(array)
        # for i in array:
        #     print(i)
        # for i, x in enumerate(record):
        # print(i, " : ", x[9])
        # print(tabulate(record, headers=header))
        # print('\nSales data-->\n\n',tabulate(record, headers=header), end='\n\n')
        # print(arrayDict)
        # for x in record:
        #     if x[9]
