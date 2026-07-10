class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merger=[]
        intervals.sort(key=lambda x: x[0])
        prev=intervals[0]
        for i in intervals[1:]:
            if prev[1]>=i[0]:
                prev[1] = max(prev[1], i[1])
            else:
                merger.append(prev)
                prev = i
        merger.append(i)
        return merger
    
y=Solution()    
result=y.merge([[1,3],[2,6],[8,10],[15,18]])
print(result)  