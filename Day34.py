Day 34 — Linked List

1. LeetCode 1721: Swapping Nodes in a Linked List

Problem:
Given the head of a linked list and an integer k, swap the values of the kth node from the beginning and the kth node from the end, then return the head.

Code (Python):

```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapNodes(self, head, k):
        # Step 1: Find length of the list
        length = 0
        current = head
        while current:
            length += 1
            current = current.next

        # Step 2: Locate kth node from start and end
        first = last = head
        for _ in range(k - 1):
            first = first.next
        for _ in range(length - k):
            last = last.next

        # Step 3: Swap values
        first.val, last.val = last.val, first.val

        return head
```

2. LeetCode 92: Reverse Linked List II

Problem:
Given the head of a singly linked list and positions left and right, reverse the nodes between left and right and return the head.

Code (Python):

```python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head, left, right):
        if not head or left == right:
            return head
        
        dummy = ListNode(0, head)
        prev = dummy
        
        # Move `prev` to node before `left`
        for _ in range(left - 1):
            prev = prev.next
        
        # Reverse the sublist
        reverse = None
        current = prev.next
        for _ in range(right - left + 1):
            next_node = current.next
            current.next = reverse
            reverse = current
            current = next_node
        
        # Connect reversed sublist back
        prev.next.next = current
        prev.next = reverse
        
        return dummy.next
```
