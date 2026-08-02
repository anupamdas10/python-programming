from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp=[-1]*len(nums)

        def func(index):
           
            if index < 0:
                return 0

            if index == 0:
                return nums[0]
            if dp[index]!=-1:return dp[index]


            pick = nums[index] + func(index - 2)
            no_pick = func(index - 1)

            dp[index]= max(pick, no_pick)
            return dp[index]    

        return func(len(nums) - 1)


y = Solution()
r = y.rob([1, 2, 3, 1])
print(r)