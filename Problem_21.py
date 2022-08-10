sum1=0
sum2=0
sum3=0
l=[]
for i in range(220,10000):
    for j in range(1,(i//2) + 1):
        if i%j==0:
            sum1=sum1+j
    for k in range(1,(sum1//2) + 1):
        if sum1%k==0:
            sum2=sum2+k
    if sum2==i and i!=sum1:
        print(sum1)
        l.append(sum1)
    sum1=0
    sum2=0

for z in l:
    sum3+=z
print("sum3 is:",sum3)

