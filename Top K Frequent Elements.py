class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict={}
        for i in range(len(nums)):
            if nums[i] in my_dict:
                my_dict[nums[i]]+=1
            else:
                 my_dict[nums[i]]=1   
        topk=sorted(my_dict, key=my_dict.get, reverse=True)[:k]     
        return topk
y=Solution()
r=y.topKFrequent([1,1,1,2,2,3], 2)
print(r) 




                        
     