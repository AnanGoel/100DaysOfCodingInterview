LeetCode Problems Solved Today
1. 901. Online Stock Span (Monotonic Stack)

Solution Summary:
Used a monotonic decreasing stack to efficiently compute the stock span for each day in O(1) amortized time. Each element in the stack stores:
[price, span]
For each new price, we pop all lower/equal prices and accumulate their span.

Code:

class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack[-1][1]
            self.stack.pop()
        self.stack.append([price, span])
        return span

2. 402. Remove K Digits (Greedy + Stack)

Solution Summary:
Used a greedy approach with a stack to remove digits that break increasing order, ensuring the smallest lexicographical number.

Pop larger digits when possible

Remove leading zeros

Return "0" if result becomes empty

Code:

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for digit in num:
            while k > 0 and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)

        while k > 0:
            stack.pop()
            k -= 1

        result = ''.join(stack).lstrip('0')
        return result if result else "0"
