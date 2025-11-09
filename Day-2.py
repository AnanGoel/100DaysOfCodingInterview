# 🚀 Day 2 — #100DaysOfInterviewCodingChallenge
# Focus: Fundamentals — Numbers & Logic Problems

# ----------------------------------------------
# 1️⃣ Reverse Integer (LeetCode 7)
# ----------------------------------------------

class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x_abs = abs(x)
        reversed_x = int(str(x_abs)[::-1])
        result = sign * reversed_x
        # Check 32-bit range
        if result < -2**31 or result > 2**31 - 1:
            return 0
        return result


# ----------------------------------------------
# 2️⃣ Palindrome Number (LeetCode 9)
# ----------------------------------------------

class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are not palindromes
        if x < 0:
            return False
        # Compare original and reversed string forms
        return str(x) == str(x)[::-1]


# ----------------------------------------------
# 3️⃣ Happy Number (LeetCode 202)
# ----------------------------------------------

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum(int(digit) ** 2 for digit in str(n))
        return n == 1


# ----------------------------------------------
# 4️⃣ Sum of Digits (GFG)
# ----------------------------------------------

class Solution:
    def sumOfDigits(self, n: int) -> int:
        total = 0
        while n > 0:
            total += n % 10
            n //= 10
        return total
