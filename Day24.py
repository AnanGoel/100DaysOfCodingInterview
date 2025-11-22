# Day 24 — Binary Search on Answers (Aggressive Cows / Magnetic Force)

## 🚀 Problem: 1552. Magnetic Force Between Two Balls

This problem is a classic Binary Search on Answer. We want to maximize the **minimum magnetic force** (distance) between any two placed balls.

---

## 🧠 Approach

1. **Sort the positions**.
2. Use **Binary Search** to guess the minimum force.
3. Use a helper function to check if we can place `m` balls with at least `mid` force.
4. Adjust search space based on feasibility.

Time Complexity: **O(n log M)**

---

## 🧩 Python Code (Clean & Commented)

```python
class Solution:
    def maxDistance(self, position, m):
        # Step 1: Sort all basket positions
        position.sort()

        # Check if we can place m balls with at least min_force distance
        def can_place(min_force):
            count = 1
            last = position[0]

            for i in range(1, len(position)):
                if position[i] - last >= min_force:
                    count += 1
                    last = position[i]
                if count == m:
                    return True
            return False

        # Step 2: Binary search for the maximum minimum force
        left, right = 1, position[-1] - position[0]
        ans = 0

        while left <= right:
            mid = (left + right) // 2

            if can_place(mid):
                ans = mid
                left = mid + 1  # try for more force
            else:
                right = mid - 1  # reduce force

        return ans
```

---

## ✅ Example

```python
sol = Solution()
print(sol.maxDistance([1,2,3,4,7], 3))               # Output: 3
print(sol.maxDistance([5,4,3,2,1,1000000000], 2))    # Output: 999999999
```

---

## 📌 Summary

* Continued Binary Search mastery.
* Solved LeetCode 1552 using the same logic as Aggressive Cows.
* Code optimized for interview readiness.

Day 24 ✔️

---

## 🧩 Python Code 2 — Aggressive Cows (GFG Version)

```python
class Solution:
    def aggressiveCows(self, stalls, k):
        # Step 1: Sort stall positions
        stalls.sort()
        
        # Helper function to check if cows can be placed
        def can_place(distance):
            count = 1  # first cow at first stall
            last = stalls[0]
            
            for i in range(1, len(stalls)):
                if stalls[i] - last >= distance:
                    count += 1
                    last = stalls[i]
                if count >= k:
                    return True
            return False

        # Step 2: Binary Search on minimum distance
        left, right = 1, stalls[-1] - stalls[0]
        ans = 0
        
        while left <= right:
            mid = (left + right) // 2

            if can_place(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans
```
