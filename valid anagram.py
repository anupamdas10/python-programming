class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       freq={}
       if len(s)!=len(t):
           return False
       for ch in s:
           freq[ch]=freq.get(ch,0)+1
       for ch in t :
           if ch not in freq:
               return False
           else:
               freq[ch]-=1
       return True

y=Solution()
r=y.isAnagram("rat","cat")
print(r)             
       