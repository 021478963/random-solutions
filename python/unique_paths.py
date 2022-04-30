class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def helper(m, n, seen = {}):
            if m > n:
                m, n = n, m
            key = (str(m) + ", " + str(n))
            if key in seen.keys():
                return seen[key]
            if m == 1 and n == 1:
                seen[key] = 1
                return 1
            if m == 0 or n == 0:
                seen[key] = 0
                return 0
            else:
                seen[key] = helper(m - 1, n, seen) + helper(m, n - 1, seen)
                return seen[key]
        return helper(m, n)
        
        