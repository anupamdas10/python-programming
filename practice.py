s="abc"
t="ahbgdc"
s1=len(s)
t1=len(t)
i=0
j=0
while i<s1 and j<t1 :
     if s[i]==t[j]:
          i=i+1
     j=j+1

if i==s1:
     print (True)
else:
     print (False)                