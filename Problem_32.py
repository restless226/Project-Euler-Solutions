'''z=3
r=1
def pd(str):
    digits=len(str)
    if digits>=10:
        return False
    for i in range(1,digits+1):
        if str(i) not in str:
            return False
    return z
def product(a,b):
    num = str(a*b)+str(a)+str(b)
    if len(num)<=9:
        return False
    q= pd(num)
l=[]
for a in range(1,100000):
    for b in range(1,100000):
        if len(str(a*b)+str(a)+str(b))>9:
            break
        p= product(a,b)
        if p==3:
            l.append(a*b)
sum=0
for x in l:
    sum+=x
print(l)
print(sum)'''

'''def pand(n):
    count=0
    for i in range(1,1000):
        y=str(i)
        for j in range(1,len(y)+1):
            if str(j) in y:
                count+=1
        if count==len(y):
            print(i)
        count=0'''

sum=0
count=0
for a in range(1,10000):
    for b in range(1,10000):
        i=str(a)+str(b)+str(a*b)
        y = str(i)
        if len(y)==9:
            for j in range(1, len(y) + 1):
                if str(j) in y:
                    count += 1
            if count == 9:
                print(i)
                sum+=(a*b)
        count = 0

print("sum is:",sum)
