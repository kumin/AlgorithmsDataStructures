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

    def printTree(self, in_node: Node):
        if in_node is None:
            return
        print("{}->{}".format(in_node.value, in_node.next))
        if in_node.next is None:
            return
        for d in in_node.next:
            self.printTree(in_node.next[d])

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


if __name__ == '__main__':
    trie = Trie()
    trie.insert("aa")
    trie.insert("a")
    for d in trie.roots:
        trie.printTree(trie.roots[d])

    print(trie.search("apple"))
    print(trie.search("app"))
    print(trie.startsWith("app"))
