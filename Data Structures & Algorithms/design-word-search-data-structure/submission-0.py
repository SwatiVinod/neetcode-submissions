class TrieNode:
    def __init__(self):
        self.children = {}
        self.fword = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.fword = True

    def search(self, word: str) -> bool:
        def dfs(node, j):
            curr = node

            for i in range(j, len(word)):
                c = word[i]
                if c == '.':
                    for child_node in curr.children.values():
                        if dfs(child_node, i+1):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            return curr.fword

        return dfs(self.root, 0)
        
