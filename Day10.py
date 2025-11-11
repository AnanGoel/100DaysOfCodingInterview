# 1. First Unique Character in a String (LeetCode 387)
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
        for i, char in enumerate(s):
            if count[char] == 1:
                return i
        return -1


# 2. First Letter to Appear Twice (LeetCode 2351)
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        seen = set()
        for char in s:
            if char in seen:
                return char
            seen.add(char)


# 3. Valid Anagram (LeetCode 242)
# Method 1: Simple Sorting
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

# Method 2: Using Counter (Optimal)
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
