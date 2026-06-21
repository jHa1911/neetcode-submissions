class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()

        while n not in s:
            s.add(n)
            n = self.squareSum(n)
            if n == 1:
                return True
        return False



    def squareSum(self, digit: int) -> int:
            sqr_sum = 0
            while digit > 0:
                sqr_sum += (digit%10)**2
                digit //= 10
            
            return sqr_sum
        