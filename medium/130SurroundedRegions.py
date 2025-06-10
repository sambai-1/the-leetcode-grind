class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        edge = [[False] * len(board[0]) for i in range(len(board))]
        
        tmp = deque()
        for i in range(len(board)):
            if board[i][0] == "O":
                tmp.append([i, 0])
            if board[i][len(board[0]) - 1] == "O":
                tmp.append((i, len(board[0]) - 1))
        for j in range(len(board[0])):
            if board[0][j] == "O":
                tmp.append([0, j])
            if board[len(board) - 1][j] == "O":
                tmp.append((len(board) - 1, j))
        
        while tmp:
            x, y = tmp.popleft()
            if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]) or board[x][y] == "X" or edge[x][y]:
                continue
            edge[x][y] = True
            tmp.append((x + 1, y))
            tmp.append((x - 1, y))
            tmp.append((x, y + 1))
            tmp.append((x, y - 1))
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O" and not edge[i][j]:
                    board[i][j] = "X"
        
        return