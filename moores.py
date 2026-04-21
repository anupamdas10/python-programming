nums=[1,2,1,3,3,4]
m=0
c=0
for i in nums:
    if c==0:
        m=i
        c=1
    else:
        if i==m:
            c=c+1
        else:
            c=c-1

print (m)                    


