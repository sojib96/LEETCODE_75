# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        fast, slow = head, head
        while fast:
            slow = slow.next
            fast = fast.next.next

        middle = slow
        prev = None
        while middle:
            temp = middle.next
            middle.next = prev
            prev = middle
            middle = temp
        
        maxSum = 0
        firstHalf = head
        secondHalf = prev
        while secondHalf:
            maxSum = max(maxSum, firstHalf.val + secondHalf.val)
            firstHalf = firstHalf.next
            secondHalf = secondHalf.next
        
        return maxSum