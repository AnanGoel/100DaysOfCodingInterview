# 🚀 Day 3 — #100DaysOfInterviewCodingChallenge
# Focus: Recursion & Mathematical Sequences

# ----------------------------------------------
# 1️⃣ Fibonacci Number (LeetCode 509)
# ----------------------------------------------

class Solution:
    def fib(self, n: int) -> int:
        """
        Compute the n-th Fibonacci number.
        F(0) = 0, F(1) = 1
        F(n) = F(n - 1) + F(n - 2)
        """
        if n <= 1:
            return n

        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b


# ----------------------------------------------
# 2️⃣ N-th Tribonacci Number (LeetCode 1137)
# ----------------------------------------------

class Solution:
    def tribonacci(self, n: int) -> int:
        """
        Compute the n-th Tribonacci number.
        T0 = 0, T1 = 1, T2 = 1
        Tn = Tn-1 + Tn-2 + Tn-3 for n >= 3
        """
        if n == 0:
            return 0
        elif n in [1, 2]:
            return 1

        t0, t1, t2 = 0, 1, 1
        for _ in range(3, n + 1):
            t0, t1, t2 = t1, t2, t0 + t1 + t2
        return t2


# ----------------------------------------------
# 3️⃣ Pow(x, n) (LeetCode 50)
# ----------------------------------------------

class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        Implement power function: x^n.
        Uses fast exponentiation for efficiency.
        """
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = -n

        result = 1
        while n:
            if n % 2 == 1:
                result *= x
            x *= x
            n //= 2
        return result
