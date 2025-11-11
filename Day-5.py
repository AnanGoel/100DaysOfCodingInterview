# Language: Python 3
# 🚀 Day 5 — #100DaysOfInterviewCodingChallenge
# Focus: Arrays & In-Place Manipulation

# --------------------------------------------------
# 1️⃣ 485. Max Consecutive Ones
# --------------------------------------------------
class Solution:
    def findMaxConsecutiveOnes(self, nums):
        count = 0
        max_count = 0

        for num in nums:
            if num == 1:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0
        return max_count


# --------------------------------------------------
# 2️⃣ 189. Rotate Array
# --------------------------------------------------
class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n  # Handle cases where k > n

        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])


# --------------------------------------------------
# 3️⃣ 628. Maximum Product of Three Numbers
# --------------------------------------------------
class Solution:
    def maximumProduct(self, nums):
        nums.sort()
        n = len(nums)
        prod1 = nums[n - 1] * nums[n - 2] * nums[n - 3]
        prod2 = nums[0] * nums[1] * nums[n - 1]
        return max(prod1, prod2)


# --------------------------------------------------
# 4️⃣ 26. Remove Duplicates from Sorted Array
# --------------------------------------------------
class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1
        return k
