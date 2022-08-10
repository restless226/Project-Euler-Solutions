'''from math import factorial

def ncr(n,r):
    if n>=r:
        return(factorial(n)/(factorial(n-r)*factorial(r)))
for l in range(3):
    for m in range(3):
        for n in range(3):
            if l!=m and m!=n and l!=n:
                x = str(l) + str(m) + str(n)
                print(x)'''

a=[]
for l in range(10):
    for m in range(10):
        for n in range(10):
            for o in range(10):
                for p in range(10):
                    for q in range(10):
                        for r in range(10):
                            for s in range(10):
                                for t in range(10):
                                    for u in range(10):
                                        if l!=m and l!=n and l!=o and l!=p and l!=q and l!=r and l!=s and l!=t and l!=u and m!=n and m!=o and m!=p and m!=q and m!=r and m!=s and m!=t and m!=u and n!=o and n!=p and n!=q and n!=r and n!=s and n!=t and n!=u and o!=p and o!=q and o!=r and o!=s and o!=t and o!=u and p!=q and p!=r and p!=s and p!=t and p!=u and q!=r and q!=s and q!=t and q!=u and r!=s and r!=t and r!=u and s!=t and s!=u and t!=u:
                                            x=str(l)+str(m)+str(n)+str(o)+str(p)+str(q)+str(r)+str(s)+str(t)+str(u)
                                            a.append(x)
print(a)
print(a[999999])

