import csv
from email import header

from numpy import record
with open('D:\\C++\\Python\\src\\python.csv') as f:
    record = csv.reader(f)
    header = next(record)
    print(header, end='\n\n')
    print('-------------------------------------------------------------------------------------------')
    for h in header:
        print(h, end='\t')
    print()
    print('-------------------------------------------------------------------------------------------')
    for x in record:
        if (int(x[2]) > 500):
            for y in x:
                print(y, end='\t')
        print()
    print('-------------------------------------------------------------------------------------------')
    print
