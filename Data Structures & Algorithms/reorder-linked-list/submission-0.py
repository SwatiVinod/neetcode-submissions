# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        second_half = slow.next
        slow.next = None

        def reverse(head):
            if not head or not head.next:
                return head
            
            new_head = reverse(head.next)

            head.next.next = head
            head.next = None

            return new_head
        
        second = reverse(second_half)
        first = head

        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2







        