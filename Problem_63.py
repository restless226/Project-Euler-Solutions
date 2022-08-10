count=0
for i in range(1,100):
        for n in range(1,100):
            k=i**n
            y=str(k)
            if len(y)==n:
                count+=1

print(count)