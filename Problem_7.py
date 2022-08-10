l=[]
num=17
while len(l)<=9995:
    for i in range(3,int(num**0.5),2):
        if (num%i==0):
            break
        else:
            l.append(num)
        num+=2
print(num)
print(l)


