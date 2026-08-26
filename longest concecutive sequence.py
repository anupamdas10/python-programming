class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
     
        longest=0
        my_set=set(nums)
      

        for num in my_set:
            if num-1 not in my_set:
                x=num
                count=1
                while x+1 in my_set:
                    count+=1
                    x+=1
                longest=max(longest,count)
        return longest        
y=Solution()
r=y.longestConsecutive( [1,0,1,2])
print(r)        
