# Author : Parishkar Singh  Python 3.10  2022
# ...............................................................
# sum of square numbers
# ...............................................................
def sumSquares(n):
    sq=0
    for i in range(1, n+1):
        sq = i**2+sq
    return sq


if __name__ == '__main__':
    n = int(input('Enter N to find the sum of squares upto it--> '))
    print(sumSquares(n))
