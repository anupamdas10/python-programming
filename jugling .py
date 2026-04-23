nums=[2,3,1,5,6,9]
n=len(nums)
k=3
for i in range(0,k):
    x=nums.pop()
    nums.insert(0,x)

print(nums)    
