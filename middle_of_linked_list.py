# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start=node=head
        le=0
        while start:
            le+=1
            start=start.next
        middle=le//2
        counter=0
        while node:
            if counter==middle:
                return node
            else:
                counter+=1
                node=node.next
        return none
