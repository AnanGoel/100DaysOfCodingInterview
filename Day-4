# 🚀 Day 4 — #100DaysOfInterviewCodingChallenge
# Focus: Arrays & In-Place Manipulation

# ----------------------------------------------
# 1️⃣ Neither Minimum nor Maximum (LeetCode 2733)
# ----------------------------------------------

class Solution:
    def findNonMinOrMax(self, nums):
        """
        Return any number that is neither the minimum nor the maximum.
        If not possible (length < 3), return -1.
        """
        if len(nums) < 3:
            return -1

        min_num = min(nums)
        max_num = max(nums)

        for num in nums:
            if num != min_num and num != max_num:
                return num

        return -1


# ----------------------------------------------
# 2️⃣ Reverse String (LeetCode 344)
# ----------------------------------------------

class Solution:
    def reverseString(self, s):
        """
        Reverse the input array of characters in-place using two pointers.
        """
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


# ----------------------------------------------
# 3️⃣ Missing Number (LeetCode 268)
# ----------------------------------------------

class Solution:
    def missingNumber(self, nums):
        """
        Given an array containing n distinct numbers from [0, n],
        find the missing number using the mathematical sum formula.
        """
        n = len(nums)
        expected_sum = n * (n + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum


# ----------------------------------------------
# 4️⃣ Move Zeroes (LeetCode 283)
# ----------------------------------------------

class Solution:
    def moveZeroes(self, nums):
        """
        Move all zeroes to the end of the array while maintaining
        the relative order of non-zero elements (in-place).
        """
        last_non_zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_non_zero], nums[i] = nums[i], nums[last_non_zero]
                last_non_zero += 1
