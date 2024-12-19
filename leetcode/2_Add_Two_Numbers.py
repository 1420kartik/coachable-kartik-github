# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Assign list 1 and list 2 to current 1 and current 2
        current_1 = l1
        current_2 = l2

        # Carry is used when the sum is greater than 9, and you carry a digit to next calculation
        carry = 0

        # Using dummy and tail node to creaet a new list and iterate over it
        dummy = ListNode("dummy")
        tail = dummy

        # We will continue the calculation until we have a num in current_1, current_2, or carry
        while current_1 or current_2 or carry:
            num_1 = current_1.val if current_1 else 0
            num_2 = current_2.val if current_2 else 0
            sum_num = num_1 + num_2 + carry

            # If the sum of the num is greater than 9, carry 1 to next calculation
            carry = 1 if sum_num > 9 else 0

            # Make a new node and assign it to new list
            digit = sum_num % 10
            tail.next = ListNode(digit)

            # Update the pointers accordingly
            tail = tail.next
            current_1 = current_1.next if current_1 else 0
            current_2 = current_2.next if current_2 else 0

        # Return the head of new list
        return dummy.next
