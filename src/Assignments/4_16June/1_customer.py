
import csv
from tabulate import tabulate
from natsort import natsorted
import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    with open("X:\\Python\\src\\Assignments\\4_16June\\supermarket.csv") as f:
        rs = csv.reader(f)
        header = next(rs)
        record = list(rs)
        # the array of dict objects where key is the invoice id and value is the customer detail row
        array = [{x[0]:x} for x in record]
        while True:
            x = input("\nEnter Choice\n1.Maximum Spent\n2.Count Customers(Payment method:- Wallet, Cash, Credit Card)\n3.Female Customers (Brought More than 5 items and spent>200)\n4.Purchase Trend (graph)  -->")
            if x == '1':
                spent = natsorted(
                    array, key=lambda x: list(x.values())[0][9])[-1]
                print(tabulate(spent.values(), headers=header))
            elif x == '2':
                cc = 0
                c = 0
                w = 0
                for i in array:
                    for key, value in i.items():
                        if value[12] == 'Credit card':
                            cc += 1
                        elif value[12] == 'Cash':
                            c += 1
                        elif value[12] == 'Ewallet':
                            w += 1
                print(
                    f"The Payment Statistics :- \n1.Credit Card->{cc}\n2.Card->{c}\n3.Wallet->{w}\nTotal Count{cc+c+w}")
            elif x == '3':
                m = 0
                for i in array:
                    for key, value in i.items():
                        # converting base 10 to base 2
                        if value[4] == 'Female' and int(float(value[7])) > 5 and int(float(value[9])) > 200:
                            m += 1
                print(
                    f'Total Females who brought more than 5 items and spent more than 200 are:- {m} ')
            elif x == '4':
                # 0 index is male and 1 index is female
                food = [0, 0]
                health = [0, 0]
                sports = [0, 0]
                fashion = [0, 0]
                electronics = [0, 0]
                home = [0, 0]
                barWidth = .125
                fig = plt.subplots(figsize=(12, 8))
                for i in array:
                    for key, value in i.items():
                        if value[4] == 'Male':
                            if value[5] == 'Health and beauty':
                                health[0] += 1
                            elif value[5] == 'Sports and travel':
                                sports[0] += 1
                            elif value[5] == 'Fashion accessories':
                                fashion[0] += 1
                            elif value[5] == 'Electronic accessories':
                                electronics[0] += 1
                            elif value[5] == 'Food and beverages':
                                food[0] += 1
                            elif value[5] == 'Home and lifestyle':
                                home[0] += 1
                        else:
                            if value[5] == 'Health and beauty':
                                health[1] += 1
                            elif value[5] == 'Sports and travel':
                                sports[1] += 1
                            elif value[5] == 'Fashion accessories':
                                fashion[1] += 1
                            elif value[5] == 'Electronic accessories':
                                electronics[1] += 1
                            elif value[5] == 'Food and beverages':
                                food[1] += 1
                            elif value[5] == 'Home and lifestyle':
                                home[1] += 1

                br1 = np.arange(len(food))
                br2 = [x + barWidth for x in br1]
                br3 = [x + barWidth for x in br2]
                br4 = [x + barWidth for x in br3]
                br5 = [x + barWidth for x in br4]
                br6 = [x + barWidth for x in br5]

                plt.bar(br1, sports, color='red', width=barWidth,
                        edgecolor='grey', label='Sports and travel')

                plt.bar(br2, food, color='green', width=barWidth,
                        edgecolor='grey', label='food and beverages')

                plt.bar(br3, fashion, color='blue', width=barWidth,
                        edgecolor='grey', label='fashion accessories')

                plt.bar(br4, health, color='cyan', width=barWidth,
                        edgecolor='grey', label='Health and Beauty')

                plt.bar(br5, electronics, color='black', width=barWidth,
                        edgecolor='grey', label='Electronics')

                plt.bar(br6, home, color='yellow', width=barWidth,
                        edgecolor='grey', label='Home and lifeStyle')
                # for checking data accuracy
                totalFemale = sports[1]+home[1] + \
                    electronics[1]+food[1]+health[1]+fashion[1]
                totalMale = sports[0]+electronics[0] + \
                    food[0]+health[0]+home[0]+fashion[0]
                print(
                    f'males buys:\nSports and travel--{sports[0]}\nElectronics--{electronics[0]}\nFood and beverages--{food[0]}\nhealth--{health[0]}\nfashion--{fashion[0]}\nHome--{home[0]}\ntotal is {totalMale}')
                print('\n\n')
                print(
                    f'Females buys:\nSports and travel--{sports[1]}\nElectronics--{electronics[1]}\nFood and beverages--{food[1]}\nhealth--{health[1]}\nfashion--{fashion[1]}\nHome--{home[1]}\ntotal is --{totalFemale}')
                plt.xlabel('Gender')
                plt.ylabel(f'Number of people-- {totalFemale+totalMale}')
                plt.xticks([r + barWidth for r in range(len(food))],
                           [f'male-{totalMale}', f'female-{totalFemale}'])
                plt.legend()
                plt.show()
