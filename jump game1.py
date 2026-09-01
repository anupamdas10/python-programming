class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_index=0
        n=len(nums)
        for i in range(0,n):
            if i>max_index:
                return False
            max_index=max(max_index,i+nums[i])
        return True
y=Solution()
r=y.canJump([2,3,1,1,4])
print(r)        