
class Solution:
    def sumOfThree(self, num):
        if num % 3 != 0:
            return []
        x = num // 3
        return [x - 1, x, x + 1]
