class Node:
    def __init__(self, val='', next=None, is_word=False):
        self.val = val
        self.next = next
        self.is_word = False


class Trie:

    def __init__(self):
        self.roots = {}

    def insert(self, word: str) -> None:
        if len(word) == 0:
            return
        if word[0] in self.roots:
            in_node = self.roots[word[0]]
            i = 1
            while in_node.next is not None and word[i] in in_node.next:
                in_node = in_node.next[word[i]]
                i += 1
                if i == len(word):
                    in_node.is_word = True
                    return
            self.buildTree(in_node=in_node, word=word[i:])
            return
        in_node = Node(val=word[0], next=None, is_word=False)
        if len(word) == 1:
            in_node.is_word = True
        self.roots[word[0]] = in_node
        self.buildTree(in_node=in_node, word=word[1:])
        return

    def buildTree(self, in_node: Node, word: str):
        for i in range(len(word)):
            new_node = Node(val=word[i], next=None)
            if i == len(word) - 1:
                new_node.is_word = True
            if in_node.next is not None:
                in_node.next[word[i]] = new_node
            else:
                in_node.next = {word[i]: new_node}

    def search(self, word: str) -> bool:
        return False

    def startsWith(self, prefix: str) -> bool:
        return False


if __name__ == '__main__':
    trie = Trie()
    trie.insert("apple")
    print(trie.roots)
