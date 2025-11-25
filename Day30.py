📅 Day 30 – #100DaysOfInterviewCodingChallenge
🧩 Problems Solved
1️⃣ Search in Linked List (GFG – Easy)

Problem: Check if a key exists in a singly linked list.
Website: GeeksForGeeks

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def searchKey(self, head, key):
        temp = head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False

2️⃣ 237. Delete Node in a Linked List (LeetCode – Medium)

Problem: Delete a node without access to the head of the list.
Website: LeetCode

class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
