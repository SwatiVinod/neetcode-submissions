
class TrieNode:
    def __init__(self):
        self.children = {}
        self.fword = None

    def __repr__(self):
        return ", ".join(list(self.children.keys()))

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows = len(board)
        cols = len(board[0])
        root = TrieNode()

        # Build TrieNode
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.fword = word
        
        result = []

        def dfs(r, c, node):
            ch = board[r][c]

            if ch not in node.children:
                return
            
            nextnode = node.children[ch]

            if nextnode.fword:
                result.append(nextnode.fword)
                nextnode.fword = None
            
            board[r][c] = '#'
            for ar, ac in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr = r + ar
                nc = c + ac

                if 0 <= nr < rows and 0 <= nc < cols:
                    dfs(nr, nc, nextnode)
            
            board[r][c] = ch


        for r in range(rows):
            for col in range(cols):
                dfs(r, col, root)

        return result
