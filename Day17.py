# Day 17 - LeetCode 1358. Number of Substrings Containing All Three Characters
# Difficulty: Medium
# Topic: Sliding Window
# Link: https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = {'a': 0, 'b': 0, 'c': 0}
        left = 0
        res = 0

        for right in range(len(s)):
            count[s[right]] += 1

            # Move the left pointer until the window no longer contains all three characters
            while all(count[char] > 0 for char in "abc"):
                count[s[left]] -= 1
                left += 1

            # Every substring ending at `right` and starting before `left`
            # forms a valid substring that contains all three characters
            res += left

        return res


# Example Test
if __name__ == "__main__":
    sol = Solution()
    print(sol.numberOfSubstrings("abcabc"))  # Output: 10
    print(sol.numberOfSubstrings("aaacb"))   # Output: 3
    print(sol.numberOfSubstrings("abc"))     # Output: 1
