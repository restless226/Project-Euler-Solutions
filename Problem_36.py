'''sum=0
for n in range(1,100000,2):
    x=str(n)
    y=x[::-1]

    p=bin(n)
    q=str(p)
    r=q[::-1]

    if x==y:
        if q==r:
            sum=sum+n

print(sum)'''

s=0
for i in range(1,1000000,2):
    if str(i)==str(i)[::-1]:
        if bin(i)[2:]==bin(i)[2:][::-1]:
            s=s+i

print(s)


