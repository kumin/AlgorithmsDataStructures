class Solution:
    def reorderSpaces(self, text: str) -> str:
        total_space = 0
        word = ''
        words = []
        for c in text:
            if c == ' ':
                total_space += 1
                if word != '':
                    words.append(word)
                    word = ''
            else:
                word += c
        if word != '':
            words.append(word)

        n = len(words)
        if n > 1:
            num_space = int(total_space / (n - 1))
            extra_space = total_space - num_space * (n - 1)
            concat_space = ' ' * num_space
            text = concat_space.join(words)
            for i in range(extra_space):
                text += ' '
        else:
            text = words[0] + ' ' * total_space

        return text


if __name__ == '__main__':
    solution = Solution()
    print(solution.reorderSpaces('this'))
