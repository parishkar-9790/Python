import csv
from tabulate import tabulate
import matplotlib.pyplot as plt

# list that will store data between 1000-2000 || 2001-5000 || 5001-10000
l1, l2, l3 = [], [], []
#list that containes ranged data
l4 = []

    
if __name__ == '__main__':
    with open('D:\\C++\\Python\\src\\Assignments\\3_4June\\SALES.csv') as f:
        rs = csv.reader(f)
        header = next(rs)
        record=list(rs)
        while True:
            x = input(
                "\nEnter Choice 1.Show All data  2.Show Data in Purchase Range 3.Plot Graph--> ")
            if x == '1':
                print('-'*100)
                print('\nSales data-->\n\n',tabulate(record, headers=header), end='\n\n')
                print('-'*100)
                
            elif x == '2':
                l4.clear()
                a, b = map(int, (input('Enter the Lower & Upper range--> ').split()))
                a, b = min(a, b), max(a, b)
                print('-'*100)
                print(f"Purchase's done in range $ {a} to {b} are---> ")
                for x in record:
                    pointer = int(float(x[6]))
                    if pointer in range(a, b):
                        l4.append(x)
                print('\nSales data-->\n\n',tabulate(l4, headers=header), end='\n\n')
                print('-'*100)
                
            elif x == '3':
                for x in record:
                    pointer = int(float(x[6]))
                    num = float(x[6])
                    if pointer in range(1000, 2000):
                        l1.append(num)
                    elif pointer in range(2001, 5000):
                        l2.append(num)
                    elif pointer in range(5001, 10000):
                        l3.append(num)
                customers = [len(l1), len(l2), len(l3)]
                purValue = [f'1000-2000-{len(l1)}', f'2001-5000-{len(l2)}', f'5001-10000-{len(l3)}']
                plt.bar(purValue, customers)
                plt.ylabel(f'No of Customers -> {len(l1)+ len(l2)+ len(l3)}')
                plt.xlabel('Purchase Value')
                plt.show()
