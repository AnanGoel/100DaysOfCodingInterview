# Day 28 — #100DaysOfInterviewCodingChallenge

## Problem 1: 32. Longest Valid Parentheses (LeetCode)

```python
class Solution:
    def longestValidParentheses(self, s):
        stack = [-1]  # Initialize with -1 to handle base for valid substring
        max_len = 0

        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)  # Push index of '('
            else:
                stack.pop()  # Pop matching '('
                if not stack:
                    stack.append(i)  # Base for next valid substring
                else:
                    max_len = max(max_len, i - stack[-1])

        return max_len
```

## Problem 2: 42. Trapping Rain Water (LeetCode)

```python
class Solution:
    def trap(self, height):
        if not height:
            return 0
        
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        water = 0

        while left < right:
            if height[left] < height[right]:
                left += 1
                left_max = max(left_max, height[left])
                water += max(0, left_max - height[left])
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water += max(0, right_max - height[right])
        
        return water
```
