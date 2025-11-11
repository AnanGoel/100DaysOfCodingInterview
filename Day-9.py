# 🧠 #100DaysOfInterviewCodingChallenge - Day 9
# String Manipulation Problems (Reverse & Palindrome)

# 1️⃣ Reverse a String
class Solution:
    def reverseString(self, s):
        return s[::-1]

# Example:
# s = "Geeks"
# Output: "skeeG"


# 2️⃣ Palindrome String
class Solution:
    def isPalindrome(self, s):
        return s == s[::-1]

# Example:
# s = "abba"
# Output: True


# 3️⃣ Valid Palindrome (LeetCode 125)
class Solution:
    def isPalindrome(self, s):
        cleaned = ''.join(ch.lower() for ch in s if ch.isalnum())
        return cleaned == cleaned[::-1]

# Example:
# s = "A man, a plan, a canal: Panama"
# Output: True
