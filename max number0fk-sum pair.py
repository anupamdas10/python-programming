

class Solution():
    def maxOperations(self, nums: List[int], k: int) -> int:
        l=0
        r=len(nums)-1
        c=0
        nums.sort()

        while l<r:
            s= nums[l]+nums[r]
            if s==k:
                l=l+1
                r=r-1
                c=c+1
            elif s<k:
                l=l+1
            else:    
                r=r-1

        return c
            
            
y=Solution()
r=y.maxOperations([1,3,3,3,4],6)
print(r)
