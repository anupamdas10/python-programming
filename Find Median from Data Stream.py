import heapq
class MedianFinder:

    def __init__(self):
        self.max_heap=[]
        self.min_heap=[]
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap,-num)
        largest=-heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap,largest)

        if len(self.max_heap)<len(self.min_heap):
            smallest=heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap,-smallest)

        

    def findMedian(self) -> float:
        if len(self.max_heap)>len(self.min_heap):
            return -self.max_heap[0]
        else:
            return(-self.max_heap[0]+self.min_heap[0])/2
        
