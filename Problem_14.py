'''l=[]
for i in range(10000,1000000):
    while
    if n%2==0:
        n=n/2
        l.append(n)

    elif n%2!=0:
        n=3*n+1
        l.append(n)'''

def collatz(n):
    count=1
    while n>1:
        if n%2==0:
            count+=1
        else:
            n=3*n+1
            count+=1
        if n==1:
            return count

#Largest number
L=0
#Largest sequence size
S=0
for i in range(1000000,10000,-1):
    n=collatz(i)
    if n>S:
        S=n
        L=i
print(L)




