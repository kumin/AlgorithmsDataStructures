class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        input_number = x
        reverse_number = 0
        while x > 0:
            reverse_number = reverse_number * 10 + x % 10
            x = x // 10
        return input_number == reverse_number


if __name__ == '__main__':
    solution = Solution()
    print(solution.isPalindrome(1111111111))
