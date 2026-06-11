class Solution:
     def findMaxAverage(self, nums, k) :
          a=sum(nums[:k])
          max_sum=a
          for i in range(k,len(nums)):
               a=a+nums[i]-nums[i-k]
               max_sum=max(max_sum,a)
               

          return max_sum/k
     

y=Solution()
r=y.findMaxAverage([1,12,-5,-6,50,3],4)     
print(r) 