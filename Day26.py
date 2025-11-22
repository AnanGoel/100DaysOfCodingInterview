# Day 26 — #100DaysOfInterviewCodingChallenge

## Problem 1: Valid Parentheses (LeetCode 20)

```python
class Solution:
    def isValid(self, s):
        stack = []
        pair = {')': '(', ']': '[', '}': '{'}
        
        for ch in s:
            if ch in pair:
                if stack and stack[-1] == pair[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        
        return len(stack) == 0
```

## Problem 2: Min Stack (LeetCode 155)

````python
class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val):
        self.stack.append(val)
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)

    def pop(self):
        val = self.stack.pop()
        if val == self.minStack[-1]:
            self.minStack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minStack[-1]
```}
````
