from math import factorial

i=0
def ncr(n,r):
    return(factorial(n)/(factorial(n-r)*factorial(r)))

for x in range(1,101):
    for y in range(1,x+1):
        if ((ncr(x,y))>1000000):
            i=i+1

