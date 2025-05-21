from functools import lru_cache
class Solution:
    def climbStairs(self, n: int) -> int:
        @lru_cache(None)

        def helper(i):
            if i<=2:
                return i
            
            return helper(i-1)+helper(i-2)
            
        return helper(n)
        