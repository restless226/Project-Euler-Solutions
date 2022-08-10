'''n=3
fact=1
x=str(n)
while True:
    for j in x:
        for i in range(1,n+1):
            fact=fact*i
            i=i-1'''

from math import factorial
x=[factorial(0),factorial(1),factorial(2),factorial(3),factorial(4),factorial(5),factorial(6),factorial(7),factorial(8),factorial(9)]

def digits_sum(n):
    s=0
    while n>0:
        s+=x[n%10]
        n=n//10
    return s

number=0
for i in range(3,1000000):
    if digits_sum(i)==i:
        number+=i

print(number)



