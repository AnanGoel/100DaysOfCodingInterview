# Day 16 - LeetCode 424. Longest Repeating Character Replacement
# Difficulty: Medium
# Topic: Sliding Window
# Link: https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_freq = 0
        left = 0
        res = 0
        
        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_freq = max(max_freq, count[s[right]])
            
            # If window becomes invalid (too many replacements needed)
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
            
            res = max(res, right - left + 1)
        
        return res


# Example Test
if __name__ == "__main__":
    sol = Solution()
    print(sol.characterReplacement("ABAB", 2))  # Output: 4
    print(sol.characterReplacement("AABABBA", 1))  # Output: 4
