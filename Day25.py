# Day 25 — Stack and Next Greater Element (Monotonic Stack)

## 🚀 Today’s Topics

* Implementing **Stack using Array**
* Solving **Next Greater Element** using a **Monotonic Stack**

---

# 🧩 1️⃣ Implement Stack Using Array (GFG Version)

```python
class myStack:

    def __init__(self, n):
        self.size = n
        self.arr = [0] * n
        self.top = -1

    # Push element x
    def push(self, x):
        if self.top == self.size - 1:
            return    # Stack is full
        self.top += 1
        self.arr[self.top] = x

    # Pop top element
    def pop(self):
        if self.top == -1:
            return -1
        val = self.arr[self.top]
        self.top -= 1
        return val

    # Peek top element
    def peek(self):
        if self.top == -1:
            return -1
        return self.arr[self.top]

    # Check if empty
    def isEmpty(self):
        return self.top == -1

    # Check if full
    def isFull(self):
        return self.top == self.size - 1
```

---

# 🧩 2️⃣ Next Greater Element (Monotonic Stack)

```python
class Solution:
    def nextLargerElement(self, arr, n=None):
        # Support both GFG driver format and custom calls
        if n is None:
            n = len(arr)

        stack = []
        result = [-1] * n

        # Traverse from right to left
        for i in range(n - 1, -1, -1):
            # Pop all elements <= current
            while stack and stack[-1] <= arr[i]:
                stack.pop()

            # Next greater exists
            if stack:
                result[i] = stack[-1]

            # Push current
            stack.append(arr[i])

        return result
```

---

# ✅ Summary

* Completed Stack implementation using arrays.
* Solved Next Greater Element using a **Monotonic Stack**.
* Ensured GFG compatibility for all function signatures.

Day 25 ✔️
