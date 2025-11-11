# 🚀 Day 13 of #100DaysOfInterviewCodingChallenge
# 🧩 Topic: Sliding Window — Maximum Subarray Problems
# 📚 Problems Covered:
# 1️⃣ Max Sum Subarray of Size K (GFG)
# 2️⃣ Maximum Sum of Distinct Subarrays with Length K (LeetCode 2461)

# ----------------------------------------
# ✅ Problem 1: Max Sum Subarray of Size K
# Difficulty: Easy
# Platform: GeeksforGeeks
# Approach: Sliding Window (O(n))
# ----------------------------------------

class Solution1:
    def maxSubarraySum(self, arr, k):
        n = len(arr)
        if n < k:
            return 0
        
        # Compute sum of first window
        window_sum = sum(arr[:k])
        max_sum = window_sum

        # Slide the window
        for i in range(k, n):
            window_sum += arr[i] - arr[i - k]
            max_sum = max(max_sum, window_sum)
        
        return max_sum


# Example Test
if __name__ == "__main__":
    arr = [100, 200, 300, 400]
    k = 2
    print("Max Sum Subarray of Size K:", Solution1().maxSubarraySum(arr, k))  # Output: 700


# ----------------------------------------
# ✅ Problem 2: Maximum Sum of Distinct Subarrays with Length K
# Difficulty: Medium
# Platform: LeetCode (2461)
# Approach: Sliding Window + HashMap for distinct tracking (O(n))
# ----------------------------------------

class Solution2:
    def maximumSubarraySum(self, nums, k):
        n = len(nums)
        seen = {}
        current_sum = 0
        max_sum = 0
        left = 0

        for right in range(n):
            # Add new element
            current_sum += nums[right]
            seen[nums[right]] = seen.get(nums[right], 0) + 1

            # If window exceeds size k, remove leftmost element
            if right - left + 1 > k:
                seen[nums[left]] -= 1
                if seen[nums[left]] == 0:
                    del seen[nums[left]]
                current_sum -= nums[left]
                left += 1

            # If window is valid and all elements are distinct
            if right - left + 1 == k and len(seen) == k:
                max_sum = max(max_sum, current_sum)

        return max_sum


# Example Test
if __name__ == "__main__":
    nums = [1, 5, 4, 2, 9, 9, 9]
    k = 3
    print("Maximum Sum of Distinct Subarray:", Solution2().maximumSubarraySum(nums, k))  # Output: 15
