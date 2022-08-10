count=1
for i in range(3):
    for j in range(1+(200-100*i)//50):
        for k in range(1+(200-100*i-50*j)//20):
            for l in range(1+(200-100*i-50*j-20*k)//10):
                for m in range(1+(200-100*i-50*j-20*k-10*l)//5):
                    for n in range(1+(200-100*i-50*j-20*k-10*l-5*m)//2):
                        for p in range(1+(200-100*i-50*j-20*k-10*l-5*m-2*n)//1):
                            if 200==(i*100)+(j*50)+(20*k)+(10*l)+(5*m)+(2*n)+(1*p):
                                count+=1

print(count)