📚 Day 32 – Linked List Mastery (Interview Preparation)

Today's focus was on solving two of the most important Linked List interview questions from LeetCode, strengthening pointer manipulation and pattern recognition skills.

✅ Problems Solved
🔹 1) 206. Reverse Linked List (LeetCode – Easy)

Problem:
Reverse a singly linked list and return the reversed list.

Approach:
Used 3 pointers (prev, curr, next) to reverse the list in-place.

Time Complexity: O(n)
Space Complexity: O(1)

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev

🔹 2) 234. Palindrome Linked List (LeetCode – Easy)

Problem:
Check if a linked list is a palindrome.

Approach:

Use slow & fast pointers to find the middle

Reverse the second half

Compare both halves

Time Complexity: O(n)
Space Complexity: O(1)

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        # Find middle
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        # Compare both halves
        left = head
        right = prev

        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True
