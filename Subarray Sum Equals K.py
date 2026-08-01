class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        prefix_sum=0
        curr_sum=0
        prefix={0:1}

        for i in nums:
            curr_sum+=i
            count+=prefix.get(curr_sum-k,0)
            prefix[curr_sum]=prefix.get(curr_sum,0)+1

        return count
y=Solution()
r=y.subarraySum([1,2,1,2],3)
print(r)    