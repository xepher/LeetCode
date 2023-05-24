# https://leetcode.com/problems/string-to-integer-atoi/
# Python List


class Solution:
    def myAtoi(self, str: str) -> int:
        numberList = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        isValid = True
        isNegtive = False
        isStartCount = False
        isFoundWhiteSpaceAfterStart = False
        array = []
        result = 0
        for c in str:
            if c == " ":
                if isStartCount:
                    isFoundWhiteSpaceAfterStart = True
                    isValid = True
                    break
                continue
            elif c == "-":
                if isStartCount:
                    isValid = True
                    break
                isStartCount = True
                isNegtive = True
            elif c == "+":
                if isStartCount:
                    isValid = True
                    break
                isStartCount = True
            elif c in numberList:
                if isFoundWhiteSpaceAfterStart:
                    isValid = False
                    break
                if isStartCount == False:
                    if len(array) == 0:
                        isStartCount = True
                array.append(numberList.index(c))
            else:
                if isStartCount:
                    break
                if len(array) == 0:
                    isValid = False
                    break
        if len(array) == 0 or not isValid:
            return result
        array.reverse()
        for index, value in enumerate(array):
            result = result + value * 10**index
        if isNegtive:
            result = 0 - result
            if result < 0 - 2**31:
                result = 0 - 2**31
        elif result > 2**31 - 1:
            result = 2**31 - 1

        return result


if __name__ == '__main__':
    print(Solution().myAtoi("123  word"))  # 123
    print(Solution().myAtoi("-123  word"))  # -123
    print(Solution().myAtoi("+123  word"))  # 123
    print(Solution().myAtoi("+$23  word"))  # 0
    print(Solution().myAtoi("word  123"))  # 0
    print(Solution().myAtoi("word  -123"))  # 0
    print(Solution().myAtoi("word  +123"))  # 0
    print(Solution().myAtoi("word  +$23"))  # 0
    print(Solution().myAtoi("1@3  word"))  # 1
    print(Solution().myAtoi("-1@3  word"))  # -1
    print(Solution().myAtoi("+1@3  word"))  # 1
    print(Solution().myAtoi("+$1@3  word"))  # 0
    print(Solution().myAtoi("word  1@3"))  # 0
    print(Solution().myAtoi("word  -1@3"))  # 0
    print(Solution().myAtoi("word  +1@3"))  # 0
    print(Solution().myAtoi("word  +$1@3"))  # 0
    print(Solution().myAtoi("42"))  # 42
    print(Solution().myAtoi("   -42"))  # -42
    print(Solution().myAtoi("4193 with words"))  # 4193
    print(Solution().myAtoi("words and 987"))  # 0
    print(Solution().myAtoi("-91283472332"))  # -2147483648
    print(Solution().myAtoi("+2"))  # 2
    print(Solution().myAtoi("+-2"))  # 0
    print(Solution().myAtoi("+0 123"))  # 0
    print(Solution().myAtoi("+0123 "))  # 123
    print(Solution().myAtoi("-5-"))  # -5
