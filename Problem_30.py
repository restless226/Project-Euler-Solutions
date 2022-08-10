add=0
def power(s):
    sum=0
    l=len(s)
    for i in range(l):
        num=(int(s[i])**5)
        sum=sum+num
    return sum

for i in range(10,1000000):
    s=str(i)
    x=power(s)
    if  x==i:
        add=add+x

print(add)