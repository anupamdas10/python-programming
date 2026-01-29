class compass:
    def funcr(self,s):
        i=0
        j=len(s)
        o=[]
        while i<(j-1):
            if s[i]==s[i+1]:
                o.append(s[i])
            i=i+1
        o.append(s[i])
        return"".join(o)
y=compass()
r=y.funcr("wwwaabccadd")
print(r)            
