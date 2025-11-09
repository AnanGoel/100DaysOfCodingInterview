#1 Area Of Circle

import math
class Solution:
    def calculateArea(self, r):
        # r can be int or float
        return math.pi * r * r

#2 Leap Year Cheker-

class Solution:
    def checkYear (self, n):
        # Leap year is divisible by 4
        # but not divisible by 100 unless also divisible by 400
        if (n % 400 == 0) or (n % 4 == 0 and n % 100 != 0):
            return True
        else:
            return False

#3 Prime Number

import math
class Solution:
    def isPrime(self, n):
        # 1 is not a prime number
        if n <= 1:
            return False
        
        # Check divisibility up to sqrt(n)
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        
        return True

