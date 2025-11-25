🚀 Day-31 — Linked List Essentials
#100DaysOfInterviewChallenge

Today I solved two important Linked List problems from LeetCode using the Fast–Slow Pointer Technique.

🔹 1) 876. Middle of the Linked List

📌 LeetCode: https://leetcode.com/problems/middle-of-the-linked-list/

✅ Approach

Use two pointers:

slow → moves 1 step

fast → moves 2 steps
When fast reaches the end, slow is at the middle.
Automatically handles both odd and even lengths.

✔️ Code
class Solution:
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

🔹 2) 141. Linked List Cycle

📌 LeetCode: https://leetcode.com/problems/linked-list-cycle/

✅ Approach

Use Floyd’s Cycle Detection Algorithm:

Move slow by 1

Move fast by 2

If they ever meet → cycle exists

If fast reaches NULL → no cycle

✔️ Code
class Solution:
    def hasCycle(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
