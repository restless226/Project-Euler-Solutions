n=1
m=[]
while True:
    t=n*(n+1)//2
    for i in range(1,t+1):
        if t%i==0:
            m.append(i)
            if len(m)<500:
                m.clear()
                n+=1
            elif len(m)>500:
                print(t)
                break






