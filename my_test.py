# This file is used to run and check the output

from calculator import Calculator
from calculator import Records

def sum_of_abs_n(n):
    n = abs(n)
    sum = 0
    if n == 0:
        return sum
    else:
        for i in range(1,n+1):
            sum = Calculator.add(sum,i)
        return sum

n = 100

res = sum_of_abs_n(n)
assert res == n*(n+1)/2

#print(Records.get_history())
print(res)
print(Records.get_latest_calculation())
print(Records.get_latest_record())