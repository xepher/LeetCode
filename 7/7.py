# https://leetcode.com/problems/reverse-integer/


class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        isNegative = False
        isRemovedZero = False
        if x < 0:
            isNegative = True
        orignal_list = []
        number = abs(x)
        while number > 0:
            orignal_list.append(number % 10)
            number = number // 10
        for digit in orignal_list:
            if not isRemovedZero:
                if(digit == 0):
                    continue
                else:
                    isRemovedZero = True
            result = result*10 + digit
        if isNegative:
            result = 0 - result
        if 0 - 2**31 < result < 2**31 - 1:
            return result
        else:
            return 0


if __name__ == '__main__':
    print(Solution().reverse(1534236469))
