class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        a, b, c = 1, 1, 1

        for i in range(1, m + n - 1):
            a *= i

        for j in range(1, m):
            b *= j

        for k in range(1, n):
            c *= k

        return a / b / c