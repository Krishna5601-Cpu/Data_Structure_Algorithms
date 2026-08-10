class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum = 0
        product = 1
        rem = 0
        while n != 0:
            rem = n % 10
            sum = sum + rem
            product = product * rem
            n = n / 10

        return product - sum
