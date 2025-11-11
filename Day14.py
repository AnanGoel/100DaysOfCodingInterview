# Day 14 – #100DaysOfInterviewCodingChallenge
# Topic: Sliding Window Problems
# Repository: https://github.com/AnanGoel/100DaysOfCodingInterview

# -----------------------------------------------------------
# Problem 1: First negative integer in every window of size K
# Difficulty: Medium
# -----------------------------------------------------------

from collections import deque

class Solution:
    def printFirstNegativeInteger(self, arr, k):
        n = len(arr)
        q = deque()
        res = []

        # Traverse the first window of size k
        for i in range(k):
            if arr[i] < 0:
                q.append(i)

        # Process rest of the windows
        for i in range(k, n):
            res.append(arr[q[0]] if q else 0)

            # Remove elements out of this window
            while q and q[0] <= i - k:
                q.popleft()

            # Add the current element if it’s negative
            if arr[i] < 0:
                q.append(i)

        # Add result for last window
        res.append(arr[q[0]] if q else 0)
        return res


# -----------------------------------------------------------
# Problem 2: Sliding Window Maximum
# Difficulty: Hard
# LeetCode 239
# -----------------------------------------------------------

from collections import deque

class Solution2:
    def maxSlidingWindow(self, nums, k):
        n = len(nums)
        if not nums:
            return []

        q = deque()
        res = []

        for i in range(n):
            # Remove indices out of the current window
            while q and q[0] <= i - k:
                q.popleft()

            # Maintain decreasing order in deque
            while q and nums[q[-1]] < nums[i]:
                q.pop()

            q.append(i)

            # Record the max for windows of size k
            if i >= k - 1:
                res.append(nums[q[0]])

        return res


# -----------------------------------------------------------
# Example Test Runs
# -----------------------------------------------------------

if __name__ == "__main__":
    ob1 = Solution()
    arr = [-8, 2, 3, -6, 10]
    k = 2
    print("First negative in each window:", ob1.printFirstNegativeInteger(arr, k))

    ob2 = Solution2()
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print("Max in each sliding window:", ob2.maxSlidingWindow(nums, k))
