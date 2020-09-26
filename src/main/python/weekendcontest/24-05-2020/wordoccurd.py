class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        str_split = sentence.split(' ')
        for i in range(len(str_split)):
            if str_split[i].startswith(searchWord):
                return i+1

        return -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.isPrefixOfWord('i use triple pillow', 'pill'))
