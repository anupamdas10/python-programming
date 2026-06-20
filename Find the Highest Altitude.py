class Solution:
    def largestAltitude(self,gain) :
        alt=0
        max_alt=0
        for i in range(len(gain)):
            alt=alt+gain[i]
            max_alt=max(max_alt,alt)
        return max_alt

y=Solution()
r=y.largestAltitude([-5,1,5,0,-7])
print(r)