# 🚀 Day 6 — #100DaysOfInterviewCodingChallenge

# 1️⃣ Sort Colors (LeetCode 75)
# Problem: Sort an array containing 0s, 1s, and 2s in-place.
class Solution:
    def sortColors(self, nums):
        low, mid, high = 0, 0, len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
        return nums

# Example:
# nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]


# 2️⃣ Majority Element (LeetCode 169)
# Problem: Find the element that appears more than n/2 times.
class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        return candidate

# Example:
# nums = [2,2,1,1,1,2,2]
# Output: 2


# 3️⃣ Maximum Subarray (LeetCode 53)
# Problem: Find the contiguous subarray with the largest sum.
class Solution:
    def maxSubArray(self, nums):
        max_sum = current_sum = nums[0]
        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        return max_sum

# Example:
# nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6


# 4️⃣ Two Sum - Pair with Given Sum (GFG)
# Problem: Determine if there exist two distinct indices whose sum equals target.
class Solution:
    def twoSum(self, arr, target):
        seen = set()
        for num in arr:
            complement = target - num
            if complement in seen:
                return True
            seen.add(num)
        return False

# Example:
# arr = [0, -1, 2, -3, 1], target = -2
# Output: True
