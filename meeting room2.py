import heapq
class Solution:
    def meetingroom(self,intervals):
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[0])
        room=[]
        for start,end in intervals:
            if room and room[0]<=start:
                heapq.heappop(room)
                
            heapq.heappush(room,end)
        return len(room)       
y=Solution()
r=y.meetingroom([[0,30],[5,10],[15,20]])     
print(r)
        