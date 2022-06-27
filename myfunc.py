from operator import truediv
from pickle import FALSE


def isprime(number):
    if number<0 or number in (0,1): return False
    for element in range(2,number): #[2,3,4,5,6,7,8]
        if (number%element==0): return False
    return True

def add(a,b):
    return a+b

def divide(a,b):
    return a/b