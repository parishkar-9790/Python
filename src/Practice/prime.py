import math

def isprime(a):
    for i in range(2,int(a/2)):
        if(i**2>a):
            break
        if(a%i==0):
            return False
    return True

print(isprime(19))