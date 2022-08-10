l1=[]
l2=[]
l3=[]
l4=[]
total=0
number=0
sum=0

for i in range(12,28124):
    for j in range(1,(i//2) + 1):
        if i%j==0:
            sum+=j
    if sum>i:
        l1.append(i)
        l2.append(i)
    sum=0

for p in l1:
    for q in l2:
        number=p+q
        if number<28124:
            l3.append(number)

for x in range(1,28124):
    if x not in l3:
        l4.append(x)

for y in l4:
    total+=y

print(total)

