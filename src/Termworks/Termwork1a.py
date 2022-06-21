# Author : Parishkar Singh  Python 3.10 2022
# ...............................................................
# Sieve Of Eratosthenes
# ...............................................................
# Termwork 1
# ...............................................................

def SOE(n):
    a = [True for i in range(n+1)]

    for i in range(2, n+1):
            for j in range(2, n+1):
                if i*j >= n+1:
                    break
                a[i*j] = False
    for i in range(2, n+1):
        if a[i] == True:
            print(i)


if __name__ == '__main__':
    x = int(input("Enter the upto number"))
    SOE(x)
