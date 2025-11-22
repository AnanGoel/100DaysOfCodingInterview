# Day 23 — Binary Search on Answer (Capacity Problems)
Today I practiced two classic **Binary Search on Answer** problems that revolve around checking feasibility under constraints.  
These are common in system design, load distribution, and real-world optimization.

# Problems:
1. **875. Koko Eating Bananas**  
2. **1011. Capacity To Ship Packages Within D Days**

---

# --------------------------------------------------
# 875. Koko Eating Bananas
# --------------------------------------------------

# Idea:
# - Koko wants to eat all bananas in h hours.
# - Eating speed k must be minimized.
# - Use binary search on k (1 → max(piles)).
# - Check if a given speed allows finishing within h hours.

class Solution875:
    def minEatingSpeed(self, piles, h):
        import math
        
        left, right = 1, max(piles)
        
        def canFinish(speed):
            hours = 0
            for p in piles:
                hours += math.ceil(p / speed)
            return hours <= h
        
        while left < right:
            mid = (left + right) // 2
            if canFinish(mid):
                right = mid
            else:
                left = mid + 1
        
        return left


# --------------------------------------------------
# 1011. Capacity To Ship Packages Within D Days
# --------------------------------------------------

# Idea:
# - Ship must carry packages (in order) within D days.
# - Capacity must be minimized but >= max(weights).
# - Binary search on ship capacity.
# - Check how many days a given capacity needs.

class Solution1011:
    def shipWithinDays(self, weights, days):
        left, right = max(weights), sum(weights)
        
        def canShip(cap):
            used_days = 1
            curr = 0
            
            for w in weights:
                if curr + w > cap:
                    used_days += 1
                    curr = w
                    if used_days > days:
                        return False
                else:
                    curr += w
            
            return True
        
        while left < right:
            mid = (left + right) // 2
            if canShip(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
