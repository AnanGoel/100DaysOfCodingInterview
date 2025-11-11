# Day 12 - #100DaysOfCodingInterview
# GitHub: https://github.com/AnanGoel/100DaysOfCodingInterview

# ------------------------------
# 1️⃣ LeetCode 575. Distribute Candies
# ------------------------------
# Alice has n candies, each with a type. She can only eat n/2 candies.
# We need to find the maximum number of *different* candy types she can eat.

class Solution1:
    def distributeCandies(self, candyType: list[int]) -> int:
        # Count unique candy types
        unique_types = len(set(candyType))
        # She can eat at most n/2 candies
        return min(unique_types, len(candyType) // 2)

# Example:
# candyType = [1,1,2,2,3,3]
# Output: 3


# ------------------------------
# 2️⃣ LeetCode 349. Intersection of Two Arrays
# ------------------------------
# Given two integer arrays, return their intersection (unique elements only).

class Solution2:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # Convert both arrays to sets to remove duplicates
        # Find common elements using intersection '&'
        return list(set(nums1) & set(nums2))

# Example:
# nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]  (order may vary)
