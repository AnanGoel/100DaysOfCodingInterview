🚀 Day 29 — #100DaysOfInterviewCodingChallenge

Today I focused on implementing fundamental data structures using other data structures — an important skill for interviews.
Solved 3 problems from LeetCode.

📘 232. Implement Queue using Stacks (LeetCode – Easy)
class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        self._shift()
        return self.s2.pop()

    def peek(self) -> int:
        self._shift()
        return self.s2[-1]

    def empty(self) -> bool:
        return not self.s1 and not self.s2

    def _shift(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())

📘 225. Implement Stack using Queues (LeetCode – Easy)
from collections import deque

class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0

📘 622. Design Circular Queue (LeetCode – Medium)
class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.q = [-1] * k
        self.front = 0
        self.rear = -1
        self.count = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % self.size
        self.q[self.rear] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.q[self.front]

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.q[self.rear]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.size
