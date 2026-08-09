class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
     left=1
     right=max(piles)
     while left<=right:
        mid=(left+right)//2
        hour=0
        for pile in piles:
           hour+=(pile+mid-1)//mid
        if hour<=h:
           right=mid-1
        else:
           left=mid+1
     return left
y=Solution()
r=y.minEatingSpeed([3,6,7,11],8)
print(r)                
           