'''t=[]
p=[]
h=[]
l=[]

n=2000
while True:
    T=n*(n+1)/2
    t.append(T)

    P=n*(3*n-1)/2
    p.append(P)

    H=n*(2*n-1)
    h.append(H)

    for i in t:
        if (i in p and i in h):
                        l.append(i)
                        print(max(l))
                        break
        else:
            n+=1'''


