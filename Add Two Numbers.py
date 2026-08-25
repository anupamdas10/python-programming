from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        curr=dummy
        carry=0

        while l1 is not None or l2 is not None or carry !=0:
            if l1 is not None:
                x=l1.val
            else:
                x=0
            if l2 is not None:
                y=l2.val
            else:
                y=0        

            sum=x+y+carry
            carry=sum//10
            curr.next=ListNode(sum%10)
            curr=curr.next

            if l1 is not None:
                l1=l1.next
            if l2 is not None:
                l2=l2.next
        return dummy.next        
# Create first linked list: 2 → 4 → 3
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

# Create second linked list: 5 → 6 → 4
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)


# Create Solution object
y = Solution()

# Call function
r = y.addTwoNumbers(l1, l2)


# Print the result
while r is not None:
    print(r.val, end=" ")
    r = r.next                        