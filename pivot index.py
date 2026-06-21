class Solution:
    def pivotIndex(self, nums) :
        left_sum=0
        total_sum=sum(nums)
        for i in range(len(nums)):
            right_sum=(total_sum-left_sum-nums[i])
            if left_sum==right_sum:
                return i
            left_sum=left_sum+nums[i]
        return -1
    
y=Solution()
r=y.pivotIndex([1,7,3,6,5,6]) 
print(r)   