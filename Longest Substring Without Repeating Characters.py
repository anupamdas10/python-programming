class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        right=0
        max_c=0
        my_dict={}
        n=len(s)
        while right<n:
            if s[right] in my_dict:
                left=max(my_dict[s[right]]+1,left)
                max_c=max(max_c,right-left+1)
            my_dict[s[right]]=right
            right+=1
          
        return max_c        
y=Solution()    
r=y.lengthOfLongestSubstring("abcabcbb")
print(r)