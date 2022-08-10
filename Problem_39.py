l1=[]
l2=[]
l3=[]

l4=[]

#greatest number of solutions
greatest=0

for a in range(1,999):
    for b in range(1,999):
        if a+b<1000:
            c=(a**2 + b**2)**0.5
            if c%1==0:
                p=a+b+c
                if p<1000:
                    l4.append(p)
                    l1.append(a)
                    l2.append(b)
                    l3.append(c)

                    total=len(l1)+len(l2)+len(l3)/3

                    if total>greatest:
                        greatest=total
                        print(greatest)
                        print(p)
                        print()

                l1.clear()
                l2.clear()
                l3.clear()




