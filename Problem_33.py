l1=[]
l2=[]
for i in range(10,100):
    for j in range(i+1,100):
        if i%10!=0 and j%10!=0 :

            m=i//10
            n=j%10

            u=i%10
            v=j//10

            if u==v:
                p=i/j
                q=m/n

                if p==q:
                    l1.append(i)
                    l2.append(j)

n=1
d=1

for a in l1:
    n=n*a
for b in l2:
    d=d*b

print(l1)
print(l2)

print(n)
print(d)
print(d/n)
