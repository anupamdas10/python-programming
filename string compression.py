class Solution:
    def compress(self, chars: List[str]) -> int:
     i=0
     write=0
     while i<len(chars):
        current=chars[i]
        j=i

        while j <len(chars) and current==chars[j]:
           j+=1
        count=j-i 

        chars[write]=current
        write+=1

        if count>1:
           for digit in str(count):
              chars[write]=digit
              write+=1
        i=j       
     return write  

y=Solution()
r=y.compress(["a","a","b","b","c","c","c"])
print(r)        
