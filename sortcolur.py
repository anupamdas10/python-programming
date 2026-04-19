nums=[0,2,1,1,2,0,1,2,0,1]
n=len(nums)
low=0
mid=0
high=(len(nums)-1)

while mid<=high:
    if nums[mid]==0:
        nums[mid],nums[low]=nums[low],nums[mid]
        low=low+1
        mid=mid+1

    elif nums[mid]==1:
        mid=mid+1

    else:
        nums[mid],nums[high]=nums[high],nums[mid]
        high=high-1

print(nums)                