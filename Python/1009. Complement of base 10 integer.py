class Solution(object):
    def bitwiseComplement(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 1

        m = n
        mask = 0

        while m != 0:
            mask = (mask << 1) | 1
            m = m >> 1

        return (~n) & mask
