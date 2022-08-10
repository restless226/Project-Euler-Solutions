dict={0:len("zero"),1:len("one"),2:len("two"),3:len("three"),4:len("four"),5:len("five"),6:len("six"),7:len("seven"),8:len("eight"),9:len("nine"),10:len("ten"),11:len("eleven"),12:len("twelve"),13:len("thirteen"),14:len("fourteen"),15:len("fifteen"),16:len("sixteen"),17:len("seventeen"),18:len("eighteen"),19:len("nineteen"),20:len("twenty"),40:len("thirty"),50:len("forty"),60:len("sixty"),70:len("seventy"),80:len("eighty"),90:len("ninenty"),100:len("hundred")}


sum1=0
sum2=0
sum3=0
sum4=0
sum5=0
sum6=0
for i in range(1,1001):
    y=str(i)

    if len(y)==1:
        sum1 = sum1 + dict[i]

    if len(y)==2:
        if i%10!=0:
            r=i%10
            sum3=sum3+dict[r]

            i=i//10
            m=10*i
            sum4= sum4+dict[m]

        elif i%10==0:
            sum3=sum3+dict[i]

    if len(y)==3:
        if i%100!=0:
            p=i%100
            sum2=sum2+dict[p]+3  #len("and")=3

            i=i//10
            n=i%10
            sum5=sum5+dict[n]

        elif i%100==0:
            sum5=sum5+dict[i]
        i = i // 10
        q = int(10 * i)
        sum6 = sum6 + dict[q]


total=sum1+sum2+sum3+sum4+sum5+sum6+8
#adding len("thousand")
print(total)




