l=[]
for a in range(2,101):
    for b in range(2,101):
        x=a**b
        if x in l:
            pass
        else:
            l.append(x)

print(len(l))