# Day 19 – #100DaysOfInterviewCodingChallenge
# Problems:
# 1. 69. Sqrt(x)
# 2. 367. Valid Perfect Square


class Solution:
    # 69. Sqrt(x)
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        left, right = 1, x // 2

        while left <= right:
            mid = (left + right) // 2
            sq = mid * mid

            if sq == x:
                return mid
            elif sq < x:
                left = mid + 1
            else:
                right = mid - 1

        return right

    # 367. Valid Perfect Square
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True

        left, right = 2, num // 2

        while left <= right:
            mid = (left + right) // 2
            sq = mid * mid

            if sq == num:
                return True
            elif sq < num:
                left = mid + 1
            else:
                right = mid - 1

        return False
