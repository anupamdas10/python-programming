class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       sort_t=sorted(t)
       sort_s=sorted(s)
       if len(sort_t)!=len(sort_s):
         return False

       if sort_t==sort_s:
            return True
       else:
            return False     

y=Solution()
r=y.isAnagram( "anagram","nagaram")
print(r)