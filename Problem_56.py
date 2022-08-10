def add(n):
    sum=0
    while n>0:
        sum+=n%10
        n=n//10
    return sum

x=0
for a in range(2,100):
    for b in range(2,100):
        sum=add(a**b)
        if sum>x:
            x=sum

print(x)




