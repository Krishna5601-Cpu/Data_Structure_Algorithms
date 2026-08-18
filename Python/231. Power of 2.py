class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        while n % 2 == 0:
            n //= 2
        return n == 1
    # Method 2: Bit manipulation (most efficient method)
    # return n > 0 and (n & (n - 1)) == 0
