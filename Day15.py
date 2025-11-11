# Day 15 - 3. Longest Substring Without Repeating Characters
# Difficulty: Medium
# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Initialize a set to store characters in the current window
        seen = set()
        left = 0
        max_len = 0

        # Use a sliding window approach
        for right in range(len(s)):
            # If a duplicate character is found, move left pointer until it's removed
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            # Add current character and update max length
            seen.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len
