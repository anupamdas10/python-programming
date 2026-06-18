class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        r = 0
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

        return maxi


y = Solution()
r = y.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2)
print(r)