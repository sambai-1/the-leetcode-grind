from typing import List

#pretty good dfs and dries problem. not that difficult

class Node:
    def __init__(self, val, end, word):
        self.val = val
        self.end = end
        self.word = word
        self.next = {}

class Solution:
    def findWords(self, board, words):
        root = Node(-1, False, "")
        for i in words:
            base = root
            for j in i:
                if j in base.next:
                    base = base.next[j]
                else:
                    curr = base.word
                    base.next[j] = Node(j, False, curr + j)
                    base = base.next[j]
            base.end = True

        visited = set()        
        ans = set()
        def dfs(x, y, curr):
            if (x, y) in visited or x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or (board[x][y] not in curr.next):
                return
            if board[x][y] in curr.next and curr.next[board[x][y]].end:
                ans.add(curr.next[board[x][y]].word)
                
            visited.add((x, y))
            dfs(x + 1, y, curr.next[board[x][y]])
            dfs(x - 1, y, curr.next[board[x][y]])
            dfs(x, y + 1, curr.next[board[x][y]])
            dfs(x, y - 1, curr.next[board[x][y]])
            visited.remove((x, y))
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, root)
        return list(ans)  
    
    
    board = [
  ["a","b","c","d"],
  ["s","a","a","t"],
  ["a","c","k","e"],
  ["a","c","d","n"]
]
words = ["bat","cat","back","backend","stack"]