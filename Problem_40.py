s="0"
for i in range(1,1000001):
    s=s+str(i)
d=int(s[1])*int(s[10])*int(s[100])*int(s[1000])*int(s[10000])*int(s[100000])*int(s[1000000])
print(d)