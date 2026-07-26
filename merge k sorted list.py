from heapq import heappush, heappop
# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
       heap=[]
       for i, node in enumerate(lists):
           if node:
               heappush(heap,(node.val,i,node))

       dummy=ListNode(0)
       curr=dummy

       while heap:
           val,i,node=heappop(heap)
           curr.next=node
           curr=curr.next

           if node.next:
               heappush(heap,(node.next.val,i,node.next))
       return dummy.next

y=Solution()
r=y.mergeKLists([[1,4,5],[1,3,4],[2,6]])
print(r)                    