# https://leetcode.com/problems/palindrome-number/


class Solution:
    def isPalindrome(self, x: int) -> bool:
        array = list(str(x))

        len = round(array.__len__() / 2)

        for i in range(0, len):
            try:
                start = array.pop(0)
                end = array.pop()

                if start != end:
                    return False
            except:
                pass

        return True

    # Queue and Stack version, more slower
    # def isPalindrome(self, x: int) -> bool:
    #     queue = list(str(x))
    #     stack = list(str(x))

    #     for i in range(0, queue.__len__()):
    #         q = queue.pop(0)
    #         s = stack.pop()
    #         if q != s:
    #             return False

    #     return True


if __name__ == "__main__":
    print(Solution().isPalindrome(121))  # True
    print(Solution().isPalindrome(-121))  # False
    print(Solution().isPalindrome(10))  # False
    print(Solution().isPalindrome(0))  # True
    print(Solution().isPalindrome(1000021))  # False
