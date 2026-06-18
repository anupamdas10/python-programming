class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        r = 0
        k=1
        l = 0
        maxi = 0
        z = 0
        n = len(nums)

        while r < n:
            if nums[r] == 0:
                z += 1

            while z > k:
                if nums[l] == 0:
                    z -= 1
                l += 1

            maxi = max(maxi, r - l + 1)
            r += 1

        return (maxi-1)

y = Solution()
r = y.longestOnes([0,1,1,1,0,1,1,0,1], 1)
print(r)