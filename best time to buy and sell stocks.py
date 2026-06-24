class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        max_profit=0
        min_num=0
        for i in range(0,n):
            min_num=min(min_num,prices[i])
            max_profit=max(max_profit,prices[i]-min_num)
        return max_profit    
    
y=Solution()
r=y.maxProfit([7,1,5,3,6,4])    
print(r)