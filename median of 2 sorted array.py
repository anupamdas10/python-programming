class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
      if len(nums1)>len(nums2):
         nums1,nums2=nums2,nums1

      x=len(nums1)
      y=len(nums2)

      start=0
      end=x
      while start<=end:
         px=(start+end) //2
         py=((x+y+1)//2 -px)

         maxleftx=float("-inf") if px==0 else nums1[px-1]
         maxlefty=float("-inf") if py==0 else nums2[py-1]
         minrightx=float("inf") if px==x else nums1[px]
         minrighty=float("inf") if py==y else nums2[py]

         if maxleftx<=minrighty and maxlefty<=minrightx:
            if (x+y)%2==0:
               return((max(maxleftx,maxlefty) + min(minrightx,minrighty))/2)
            else:
               return(max(maxleftx,maxlefty))
            
         elif maxleftx>minrighty:
             end=px-1
         else:
            
             start=px+1
y=Solution()
r=y.findMedianSortedArrays([1,3],[2])
print(r)       