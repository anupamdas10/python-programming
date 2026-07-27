import random
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        left=0
        right=len(nums)-1

        def randomIndex(self,left,right):
            return random.randint(left,right)

        def PartitionandreturnIndex(self,nums,pivot,left,right):
            nums[left],nums[pivot]=nums[pivot],nums[left]
            index=left+1
            for i in range(left+1,right+1):
                if nums[i]>pivot:
                    nums[index],nums[i]=nums[i],nums[index]
                    index=index+1

            nums[left],nums[index-1]=nums[index-1],nums[left]
            return index-1
        while True:
            pivot=randomIndex(self,left,right)
            pivot=PartitionandreturnIndex(self,nums,pivot,left,right)
            if pivot==k-1:
                return nums[pivot]
            elif pivot > k-1:
                right=pivot-1
            else:
                left =pivot + 1
y=Solution()
r=y.findKthLargest([3,2,1,5,6,4],2)
print(r)