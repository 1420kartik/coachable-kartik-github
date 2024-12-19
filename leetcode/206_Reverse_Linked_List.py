# Definition for singly-linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Maintaing variables to iterate over the linked list
        current = head
        prev = None

        # Iterating over the linked list
        while current is not None:
            # Saving the current's next as we it is going to point to prev
            next_node = current.next
            current.next = prev

            # Updating prev and current 
            prev = current
            current = next_node

        # Returning prev as current is now pointing to None
        return prev
