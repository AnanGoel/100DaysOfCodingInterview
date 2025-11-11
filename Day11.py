# 🚀 Day 11 — #100DaysOfInterviewCodingChallenge
# Author: Anant Goel
# Topics: Arrays, Hashmaps, Sets, Sorting
# Problems Covered:
# 1. At Least K Occurrences
# 2. Check Equal Arrays
# 3. Contains Duplicate (LeetCode 217)

# ----------------------------------------------------------
# 🧩 Problem 1: At Least K Occurrences
# Difficulty: Easy
# Description:
# Given an array, return the first element that occurs at least k times.
# If multiple such elements exist, return the one that appears first.
# If no such element exists, return -1.

# Example:
# Input: arr = [1, 7, 4, 3, 4, 8, 7], k = 2
# Output: 4

class Solution:
    def firstElementKTime(self, arr, k):
        freq = {}
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
            if freq[num] == k:
                return num
        return -1


# ----------------------------------------------------------
# 🧩 Problem 2: Check Equal Arrays
# Difficulty: Easy
# Description:
# Given two arrays of equal size, determine whether they contain the same elements.
# Order does not matter, but frequency of each element must be identical.

# Example:
# Input: a = [1, 2, 5, 4, 0], b = [2, 4, 5, 0, 1]
# Output: True

class Solution2:
    def checkEqual(self, arr1, arr2):
        if len(arr1) != len(arr2):
            return False
        return sorted(arr1) == sorted(arr2)


# ----------------------------------------------------------
# 🧩 Problem 3: Contains Duplicate (LeetCode 217)
# Difficulty: Easy
# Description:
# Given an integer array, return True if any value appears at least twice in the array.
# Otherwise, return False.

# Example:
# Input: nums = [1, 2, 3, 1]
# Output: True

class Solution3:
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))


# ----------------------------------------------------------
# ✅ Example Test Runs (for manual testing)

if __name__ == "__main__":
    # Problem 1 test
    print("🧩 Problem 1 Output:")
    print(Solution().firstElementKTime([1, 7, 4, 3, 4, 8, 7], 2))  # Expected: 4
    print(Solution().firstElementKTime([10, 8, 2], 10))  # Expected: -1

    # Problem 2 test
    print("\n🧩 Problem 2 Output:")
    print(Solution2().checkEqual([1, 2, 5, 4, 0], [2, 4, 5, 0, 1]))  # Expected: True
    print(Solution2().checkEqual([1, 2, 5], [2, 4, 15]))  # Expected: False

    # Problem 3 test
    print("\n🧩 Problem 3 Output:")
    print(Solution3().containsDuplicate([1, 2, 3, 1]))  # Expected: True
    print(Solution3().containsDuplicate([1, 2, 3, 4]))  # Expected: False
