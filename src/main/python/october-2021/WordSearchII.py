from typing import List


class Node:
    def __init__(self, value: str, next=None, is_word=False):
        self.value = value
        self.next = next
        self.is_word = is_word


class Trie:

    def __init__(self):
        self.roots = {}

    def insert(self, word: str) -> None:
        if len(word) == 0:
            return
        if word[0] in self.roots:
            in_node = self.roots[word[0]]
            i = 1
            if i >= len(word):
                in_node.is_word = True
                return
            while in_node.next is not None and word[i] in in_node.next:
                in_node = in_node.next[word[i]]
                i += 1
                if i == len(word):
                    in_node.is_word = True
                    return
            self.buildTree(in_node=in_node, word=word[i:])
            return
        in_node = Node(value=word[0], next=None, is_word=False)
        if len(word) == 1:
            in_node.is_word = True
        self.roots[word[0]] = in_node
        self.buildTree(in_node=in_node, word=word[1:])
        return

    def buildTree(self, in_node: Node, word: str):
        for i in range(len(word)):
            new_node = Node(value=word[i], next=None)
            if i == len(word) - 1:
                new_node.is_word = True
            if in_node.next is not None:
                in_node.next[word[i]] = new_node
            else:
                in_node.next = {word[i]: new_node}
            in_node = new_node

    def search(self, word: str) -> bool:
        if len(word) == 0:
            return True
        if word[0] not in self.roots:
            return False
        in_node = self.roots[word[0]]
        i = 0
        while in_node is not None:
            if in_node.is_word and i == len(word) - 1:
                return True
            i += 1
            if i >= len(word) or in_node.next is None or word[i] not in in_node.next:
                return False
            in_node = in_node.next[word[i]]

        return False

    def startsWith(self, prefix: str) -> bool:
        if len(prefix) == 0:
            return True
        if prefix[0] not in self.roots:
            return False
        in_node = self.roots[prefix[0]]
        i = 0
        while in_node is not None:
            if i == len(prefix) - 1:
                return True
            i += 1
            if i >= len(prefix) or in_node.next is None or prefix[i] not in in_node.next:
                return False
            in_node = in_node.next[prefix[i]]

        return False


class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()

        def exist(word: str) -> bool:
            n = len(board)
            m = len(board[0])
            if m * n < len(word):
                return False
            directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
            visited = [[False for j in range(m)] for i in range(n)]

            def DFS(x: int, y: int, cur_word: int, prefix_word: str) -> bool:
                if board[x][y] == word[cur_word]:
                    if cur_word == len(word) - 1:
                        return True
                    for d in directions:
                        xn = x + d[0]
                        yn = y + d[1]
                        if 0 <= xn < n and 0 <= yn < m and not visited[xn][yn]:
                            visited[xn][yn] = True
                            prefix_word += board[xn][yn]
                            trie.insert(prefix_word)
                            if DFS(xn, yn, cur_word + 1, prefix_word):
                                return True
                            # back point
                            visited[xn][yn] = False
                            prefix_word = prefix_word[:len(prefix_word) - 1]
                return False

            for i in range(n):
                for j in range(m):
                    if board[i][j] == word:
                        return True
                    visited[i][j] = True
                    if DFS(i, j, 0, word[0]):
                        return True
                    visited[i][j] = False
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                trie.insert(board[i][j])
        result = []
        for word in words:
            ok = True
            for w in word:
                if not trie.search(w):
                    ok = False
                    break
            if not ok:
                continue
            if trie.startsWith(word):
                result.append(word)
                continue
            if exist(word):
                result.append(word)
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.findWords(
        [["b", "a", "b", "a", "b", "a", "b", "a", "b", "a"], ["a", "b", "a", "b", "a", "b", "a", "b", "a", "b"],
         ["b", "a", "b", "a", "b", "a", "b", "a", "b", "a"], ["a", "b", "a", "b", "a", "b", "a", "b", "a", "b"],
         ["b", "a", "b", "a", "b", "a", "b", "a", "b", "a"], ["a", "b", "a", "b", "a", "b", "a", "b", "a", "b"],
         ["b", "a", "b", "a", "b", "a", "b", "a", "b", "a"], ["a", "b", "a", "b", "a", "b", "a", "b", "a", "b"],
         ["b", "a", "b", "a", "b", "a", "b", "a", "b", "a"], ["a", "b", "a", "b", "a", "b", "a", "b", "a", "b"]],
        [
            "ababababaa", "ababababab", "ababababac", "ababababad", "ababababae", "ababababaf", "ababababag",
            "ababababah", "ababababai", "ababababaj", "ababababak", "ababababal", "ababababam", "ababababan",
            "ababababao", "ababababap", "ababababaq", "ababababar", "ababababas", "ababababat", "ababababau",
            "ababababav", "ababababaw", "ababababax", "ababababay", "ababababaz", "ababababba", "ababababbb",
            "ababababbc", "ababababbd", "ababababbe", "ababababbf", "ababababbg", "ababababbh", "ababababbi",
            "ababababbj", "ababababbk", "ababababbl", "ababababbm", "ababababbn", "ababababbo", "ababababbp",
            "ababababbq", "ababababbr", "ababababbs", "ababababbt", "ababababbu", "ababababbv", "ababababbw",
            "ababababbx", "ababababby", "ababababbz", "ababababca", "ababababcb", "ababababcc", "ababababcd",
            "ababababce", "ababababcf", "ababababcg", "ababababch", "ababababci", "ababababcj", "ababababck",
            "ababababcl", "ababababcm", "ababababcn", "ababababco", "ababababcp", "ababababcq", "ababababcr",
            "ababababcs", "ababababct", "ababababcu", "ababababcv", "ababababcw", "ababababcx", "ababababcy",
            "ababababcz", "ababababda", "ababababdb", "ababababdc", "ababababdd", "ababababde", "ababababdf",
            "ababababdg", "ababababdh", "ababababdi", "ababababdj", "ababababdk", "ababababdl", "ababababdm",
            "ababababdn", "ababababdo", "ababababdp", "ababababdq", "ababababdr", "ababababds", "ababababdt",
            "ababababdu", "ababababdv", "ababababdw", "ababababdx", "ababababdy", "ababababdz", "ababababea",
            "ababababeb", "ababababec", "ababababed", "ababababee", "ababababef", "ababababeg", "ababababeh",
            "ababababei", "ababababej", "ababababek", "ababababel", "ababababem", "ababababen", "ababababeo",
            "ababababep", "ababababeq", "ababababer", "ababababes", "ababababet", "ababababeu", "ababababev",
            "ababababew", "ababababex", "ababababey", "ababababez", "ababababfa", "ababababfb", "ababababfc",
            "ababababfd", "ababababfe", "ababababff", "ababababfg", "ababababfh", "ababababfi", "ababababfj",
            "ababababfk", "ababababfl", "ababababfm", "ababababfn", "ababababfo", "ababababfp", "ababababfq",
            "ababababfr", "ababababfs", "ababababft", "ababababfu", "ababababfv", "ababababfw", "ababababfx",
            "ababababfy", "ababababfz", "ababababga", "ababababgb", "ababababgc", "ababababgd", "ababababge",
            "ababababgf", "ababababgg", "ababababgh", "ababababgi", "ababababgj", "ababababgk", "ababababgl",
            "ababababgm", "ababababgn", "ababababgo", "ababababgp", "ababababgq", "ababababgr", "ababababgs",
            "ababababgt", "ababababgu", "ababababgv", "ababababgw", "ababababgx", "ababababgy", "ababababgz",
            "ababababha", "ababababhb", "ababababhc", "ababababhd", "ababababhe", "ababababhf", "ababababhg",
            "ababababhh", "ababababhi", "ababababhj", "ababababhk", "ababababhl", "ababababhm", "ababababhn",
            "ababababho", "ababababhp", "ababababhq", "ababababhr", "ababababhs", "ababababht", "ababababhu",
            "ababababhv", "ababababhw", "ababababhx", "ababababhy", "ababababhz", "ababababia", "ababababib",
            "ababababic", "ababababid", "ababababie", "ababababif", "ababababig", "ababababih", "ababababii",
            "ababababij", "ababababik", "ababababil", "ababababim", "ababababin", "ababababio", "ababababip",
            "ababababiq", "ababababir", "ababababis", "ababababit", "ababababiu", "ababababiv", "ababababiw",
            "ababababix", "ababababiy", "ababababiz", "ababababja", "ababababjb", "ababababjc", "ababababjd",
            "ababababje", "ababababjf", "ababababjg", "ababababjh", "ababababji", "ababababjj", "ababababjk",
            "ababababjl", "ababababjm", "ababababjn", "ababababjo", "ababababjp", "ababababjq", "ababababjr",
            "ababababjs", "ababababjt", "ababababju", "ababababjv", "ababababjw", "ababababjx", "ababababjy",
            "ababababjz", "ababababka", "ababababkb", "ababababkc", "ababababkd", "ababababke", "ababababkf",
            "ababababkg", "ababababkh", "ababababki", "ababababkj", "ababababkk", "ababababkl", "ababababkm",
            "ababababkn", "ababababko", "ababababkp", "ababababkq", "ababababkr", "ababababks", "ababababkt",
            "ababababku", "ababababkv", "ababababkw", "ababababkx", "ababababky", "ababababkz", "ababababla",
            "abababablb", "abababablc", "ababababld", "abababable", "abababablf", "abababablg", "abababablh",
            "ababababli", "abababablj", "abababablk", "ababababll", "abababablm", "ababababln", "abababablo",
            "abababablp", "abababablq", "abababablr", "ababababls", "abababablt", "abababablu", "abababablv",
            "abababablw", "abababablx", "abababably", "abababablz", "ababababma", "ababababmb", "ababababmc",
            "ababababmd", "ababababme", "ababababmf", "ababababmg", "ababababmh", "ababababmi", "ababababmj",
            "ababababmk", "ababababml", "ababababmm", "ababababmn", "ababababmo", "ababababmp", "ababababmq",
            "ababababmr", "ababababms", "ababababmt", "ababababmu", "ababababmv", "ababababmw", "ababababmx",
            "ababababmy", "ababababmz", "ababababna", "ababababnb", "ababababnc", "ababababnd", "ababababne",
            "ababababnf", "ababababng", "ababababnh", "ababababni", "ababababnj", "ababababnk", "ababababnl",
            "ababababnm", "ababababnn", "ababababno", "ababababnp", "ababababnq", "ababababnr", "ababababns",
            "ababababnt", "ababababnu", "ababababnv", "ababababnw", "ababababnx", "ababababny", "ababababnz",
            "ababababoa", "ababababob", "ababababoc", "ababababod", "ababababoe", "ababababof", "ababababog",
            "ababababoh", "ababababoi", "ababababoj", "ababababok", "ababababol", "ababababom", "ababababon",
            "ababababoo", "ababababop", "ababababoq", "ababababor", "ababababos", "ababababot", "ababababou",
            "ababababov", "ababababow", "ababababox", "ababababoy", "ababababoz", "ababababpa", "ababababpb",
            "ababababpc", "ababababpd", "ababababpe", "ababababpf", "ababababpg", "ababababph", "ababababpi",
            "ababababpj", "ababababpk", "ababababpl", "ababababpm", "ababababpn", "ababababpo", "ababababpp",
            "ababababpq", "ababababpr", "ababababps", "ababababpt", "ababababpu", "ababababpv", "ababababpw",
            "ababababpx", "ababababpy", "ababababpz", "ababababqa", "ababababqb", "ababababqc", "ababababqd",
            "ababababqe", "ababababqf", "ababababqg", "ababababqh", "ababababqi", "ababababqj", "ababababqk",
            "ababababql", "ababababqm", "ababababqn", "ababababqo", "ababababqp", "ababababqq", "ababababqr",
            "ababababqs", "ababababqt", "ababababqu", "ababababqv", "ababababqw", "ababababqx", "ababababqy",
            "ababababqz", "ababababra", "ababababrb", "ababababrc", "ababababrd", "ababababre", "ababababrf",
            "ababababrg", "ababababrh", "ababababri", "ababababrj", "ababababrk", "ababababrl", "ababababrm",
            "ababababrn", "ababababro", "ababababrp", "ababababrq", "ababababrr", "ababababrs", "ababababrt",
            "ababababru", "ababababrv", "ababababrw", "ababababrx", "ababababry", "ababababrz", "ababababsa",
            "ababababsb", "ababababsc", "ababababsd", "ababababse", "ababababsf", "ababababsg", "ababababsh",
            "ababababsi", "ababababsj", "ababababsk", "ababababsl", "ababababsm", "ababababsn", "ababababso",
            "ababababsp", "ababababsq", "ababababsr", "ababababss", "ababababst", "ababababsu", "ababababsv",
            "ababababsw", "ababababsx", "ababababsy", "ababababsz", "ababababta", "ababababtb", "ababababtc",
            "ababababtd", "ababababte", "ababababtf", "ababababtg", "ababababth", "ababababti", "ababababtj",
            "ababababtk", "ababababtl", "ababababtm", "ababababtn", "ababababto", "ababababtp", "ababababtq",
            "ababababtr", "ababababts", "ababababtt", "ababababtu", "ababababtv", "ababababtw", "ababababtx",
            "ababababty", "ababababtz", "ababababua", "ababababub", "ababababuc", "ababababud", "ababababue",
            "ababababuf", "ababababug", "ababababuh", "ababababui", "ababababuj", "ababababuk", "ababababul",
            "ababababum", "ababababun", "ababababuo", "ababababup", "ababababuq", "ababababur", "ababababus",
            "ababababut", "ababababuu", "ababababuv", "ababababuw", "ababababux", "ababababuy", "ababababuz",
            "ababababva", "ababababvb", "ababababvc", "ababababvd", "ababababve", "ababababvf", "ababababvg",
            "ababababvh", "ababababvi", "ababababvj", "ababababvk", "ababababvl", "ababababvm", "ababababvn",
            "ababababvo", "ababababvp", "ababababvq", "ababababvr", "ababababvs", "ababababvt", "ababababvu",
            "ababababvv", "ababababvw", "ababababvx", "ababababvy", "ababababvz", "ababababwa", "ababababwb",
            "ababababwc", "ababababwd", "ababababwe", "ababababwf", "ababababwg", "ababababwh", "ababababwi",
            "ababababwj", "ababababwk", "ababababwl", "ababababwm", "ababababwn", "ababababwo", "ababababwp",
            "ababababwq", "ababababwr", "ababababws", "ababababwt", "ababababwu", "ababababwv", "ababababww",
            "ababababwx", "ababababwy", "ababababwz", "ababababxa", "ababababxb", "ababababxc", "ababababxd",
            "ababababxe", "ababababxf", "ababababxg", "ababababxh", "ababababxi", "ababababxj", "ababababxk",
            "ababababxl", "ababababxm", "ababababxn", "ababababxo", "ababababxp", "ababababxq", "ababababxr",
            "ababababxs", "ababababxt", "ababababxu", "ababababxv", "ababababxw", "ababababxx", "ababababxy",
            "ababababxz", "ababababya", "ababababyb", "ababababyc", "ababababyd", "ababababye", "ababababyf",
            "ababababyg", "ababababyh", "ababababyi", "ababababyj", "ababababyk", "ababababyl", "ababababym",
            "ababababyn", "ababababyo", "ababababyp", "ababababyq", "ababababyr", "ababababys", "ababababyt",
            "ababababyu", "ababababyv", "ababababyw", "ababababyx", "ababababyy", "ababababyz", "ababababza",
            "ababababzb", "ababababzc", "ababababzd", "ababababze", "ababababzf", "ababababzg", "ababababzh",
            "ababababzi", "ababababzj", "ababababzk", "ababababzl", "ababababzm", "ababababzn", "ababababzo",
            "ababababzp", "ababababzq", "ababababzr", "ababababzs", "ababababzt", "ababababzu", "ababababzv",
            "ababababzw", "ababababzx", "ababababzy", "ababababzz"]))
