list = [n for n in range (100,1000) if n % 2 == 0]
from functools import reduce
def func(n1,n):
    return n1*n
print(reduce(func,list))