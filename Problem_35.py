l=[]
for i in range(3,100):
    for j in range(3,int(i**0.5),2):
        if i%j==0:
            break
        else:
            l.append(i)

print(l)




