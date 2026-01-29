class variable:
    def func(self,s,p):
        for i in s:
            s=s.replace(p,"")
            return s
y=variable()
r=y.func("daabcbaabcba","abc")
print(r)        