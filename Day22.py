# Day 22 — Binary Search on Answer
# Problems:
# 1. 1283. Find the Smallest Divisor Given a Threshold
# 2. 410. Split Array Largest Sum


# --------------------------------------------------
# 1283. Find the Smallest Divisor Given a Threshold
# --------------------------------------------------

class Solution1283:
    def smallestDivisor(self, nums, threshold):

        left, right = 1, max(nums)

        def compute(div):
            total = 0
            for n in nums:
                total += (n + div - 1) // div   # ceil(n/div)
            return total

        while left < right:
            mid = (left + right) // 2

            if compute(mid) <= threshold:
                right = mid
            else:
                left = mid + 1

        return left



# --------------------------------------------------
# 410. Split Array Largest Sum
# --------------------------------------------------

class Solution410:
    def splitArray(self, nums, k):

        left, right = max(nums), sum(nums)

        def canSplit(maxSum):
            count = 1
            curr = 0

            for n in nums:
                if curr + n > maxSum:
                    count += 1
                    curr = n
                    if count > k:
                        return False
                else:
                    curr += n
            return True

        while left < right:
            mid = (left + right) // 2

            if canSplit(mid):
                right = mid
            else:
                left = mid + 1

        return left
