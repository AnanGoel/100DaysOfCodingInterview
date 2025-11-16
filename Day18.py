# -------------------------------------------
# Day 18 - Binary Search (LeetCode Problems)
# -------------------------------------------
# Problems Covered:
# 1. 704. Binary Search
# 2. 278. First Bad Version
# -------------------------------------------


# ---------------------------------------------------------
# 704. Binary Search
# ---------------------------------------------------------
# Given a sorted array, return the index of the target.
# If not found, return -1.
# Time Complexity: O(log n)
# ---------------------------------------------------------

class Solution704:
    def search(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1



# ---------------------------------------------------------
# 278. First Bad Version
# ---------------------------------------------------------
# You're given an API isBadVersion(version).
# Need to find the FIRST version that is bad.
# Binary search to minimize calls.
# Time Complexity: O(log n)
# ---------------------------------------------------------

# Dummy API for representation (LeetCode provides this)
def isBadVersion(version):
    # Replace with real logic in test environment
    return version >= bad_version_global  # only for simulation


class Solution278:
    def firstBadVersion(self, n):
        left, right = 1, n
        first_bad = n

        while left <= right:
            mid = (left + right) // 2

            if isBadVersion(mid):
                first_bad = mid
                right = mid - 1
            else:
                left = mid + 1

        return first_bad



# -------------------------------------------
# Example Usage (You can remove before pushing)
# -------------------------------------------

if __name__ == "__main__":
    # 704 Example
    obj = Solution704()
    print(obj.search([-1,0,3,5,9,12], 9))  # Output: 4
    print(obj.search([-1,0,3,5,9,12], 2))  # Output: -1

    # 278 Example
    bad_version_global = 4  # Simulated bad version
    obj2 = Solution278()
    print(obj2.firstBadVersion(5))  # Output: 4
