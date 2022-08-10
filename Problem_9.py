from math import sqrt
for b in range(1,1000):
    for c in range(1,1000):
        while b<c:
            if ((1000-b)*(b+c)==1000000):
                    print(b)
                    print(c)
a=1000-(b+c)
print(a)
print(a*b*c)