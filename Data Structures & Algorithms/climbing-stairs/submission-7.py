from functools import cache

class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
        #base case 0 or -1
        if n==0:
            return 1
        elif n==-1:
            return 0
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2)