class compass:
    def func(self,s):
        i=0
        c=1
        j=len(s)
        o=[]
        while i<(j-1):
            if s[i]==s[i+1]:
                c=c+1
            else:
                o.append(s[i]+str(c))
                c=1
            i=i+1
        o.append(s[i]+str(c))       
        return "".join(o)
y=compass()
r=y.func("wwwaabccaddd")
print(r)    
