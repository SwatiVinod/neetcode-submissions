# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        def mergeTwoSortedLists(list1, list2):
            new_head = curr = ListNode()
            
            while list1 and list2:
                if list1.val <= list2.val:
                    curr.next = list1
                    list1 = list1.next
                else:
                    curr.next = list2
                    list2 = list2.next
                curr = curr.next
            
            curr.next = list1 or list2
            return new_head.next
        
        for i in range(1, len(lists)):
            lists[i] = mergeTwoSortedLists(lists[i-1], lists[i])
        
        return lists[-1]



