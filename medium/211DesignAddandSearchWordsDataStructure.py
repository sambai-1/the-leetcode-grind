class Node:
    def __init__(self, val, end):
        self.val = val
        self.end = end
        self.next = {}


class WordDictionary:

    def __init__(self):
        self.root = Node(-1, False)

    def addWord(self, word):
        base = self.root

        for i in word:
            if i in base.next:
                base = base.next[i]
            else:
                base.next[i] = Node(i, False)
                base = base.next[i]
        base.end = True

    def search(self, word):
        base = self.root
        
        def bfs(curr, word):
            if not word and curr.end:
                return True
            elif not word:
                return False

            ans = False
            for i, j in curr.next.items():
                if i == word[0] or word[0] == ".":
                    ans = ans or bfs(j, word[1:])
            return ans

        return bfs(base, word)