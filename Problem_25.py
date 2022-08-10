a=1
b=2
l=[]
while True:
    x=a+b
    y=str(x)
    a,b=b,a+b
    l.append(y)
    if len(y)==1000:
        break
print(y)
print(l.index(y))