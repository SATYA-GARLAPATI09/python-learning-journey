import math
n = int(input("Enter a positive integer: "))

class Solution:
    def checkDivisibility(self, n: int) -> bool:
        if n <= 0:
            return False

        digits = []
        original = n

        while n > 0:
            digits.append(n % 10)
            n //= 10

        sum_digits = sum(digits)
        product_digits = math.prod(digits)
        divisor = sum_digits + product_digits

        if divisor == 0:
            return False

        return original % divisor == 0


print(Solution().checkDivisibility(n))
