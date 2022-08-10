sum=17
for i in range(11,10000,2):
    for j in range(3, int(i ** 0.5), 2):
        if i%j==0 :
            break
        else:
            sum+=i
print(sum)