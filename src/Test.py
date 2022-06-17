import csv


allbooks = [{'bookid': 1000, 'title': 'DBMS', 'price': 465},
            {'bookid': 1002, 'title': 'PYTHON', 'price': 4365},
            {'bookid': 10120, 'title': 'heythere', 'price': 41265}]


def writebooks():
    with open('X:\\Python\\src\\python.csv', 'w', newline=' ')as f:
        writer = csv.writer(f)
        for x in allbooks:
            for key, value in x.items():
                writer.writerow(f'{key},{value}')


# def searchbook(price):
#     try:
#         if price <= 0:
#             raise Exception('invalid price')
#         else:
#             for book in allbooks:

#     except Exception as e:
#         for book in allbooks:
#             if book['price'] < price:
