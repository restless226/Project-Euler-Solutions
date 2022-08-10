n=int(input("enter value:"))
x=str(n)
p=len(x)
i=1
sum=0
while i<=p:
    r=n%10
    sum=sum+r
    n=n//10
    i+=1
print()
print(sum)