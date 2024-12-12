Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # Pointer One to track the node where we will insert the new list, aka 'a'
        current_1 = list1

        for i in range(a-1):
            current_1 = current_1.next

        # Pointer Two to track where the new list will point to, , aka 'b'
        current_2 = current_1

        for i in range(b - a + 2):
            current_2 = current_2.next

        # Pointer Three to track the tail of list2
        current_3 = list2

        while current_3.next:
            current_3 = current_3.next

        # Update the pointer next accordingly to merge the list
        current_1.next = list2
        current_3.next = current_2

        # Return the head of list one
        return list1
