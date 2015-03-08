class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        '''
        Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.


A sudoku puzzle...


...and its solution numbers marked in red. 
        '''
        row = [set() for i in range(9)]
        col = [set() for i in range(9)]
        cube = [set() for i in range(9)]
        blanks = []
        for i in range(9):
            for j in range(9):
                x = board[i][j]
                k = i // 3 * 3 + j // 3
                if x == '.':
                    blanks.append([i, j, k])
                    continue
                row[i].add(x)
                col[j].add(x)
                cube[k].add(x)
        self.dfs(board, blanks, 0, row, col, cube)

    def dfs(self, board, blanks, ith, row, col, cube):
        if ith == len(blanks):
            return True
        x, y, k = blanks[ith]
        for i in range(1, 10):
            c = chr(ord('0') + i)
            if c in row[x] or c in col[y] or c in cube[k]:
                continue
            row[x].add(c)
            col[y].add(c)
            cube[k].add(c)
            board[x][y] = c
            res = self.dfs(board, blanks, ith + 1, row, col, cube)
            if res:
                return True
            board[x][y] = '.'
            row[x].remove(c)
            col[y].remove(c)
            cube[k].remove(c)

    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku_usingArray(self, board):
        '''
        Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.


A sudoku puzzle...


...and its solution numbers marked in red.
        '''
        row = [[False] * 10 for i in range(9)]
        col = [[False] * 10 for i in range(9)]
        cube = [[False] * 10 for i in range(9)]
        blanks = []
        for i in range(9):
            for j in range(9):
                x = ord(board[i][j]) - ord('0')
                k = i // 3 * 3 + j // 3
                if board[i][j] == '.':
                    blanks.append([i, j, k])
                    continue
                row[i][x] = True
                col[j][x] = True
                cube[k][x] = True
        self.dfs_usingArray(board, blanks, 0, row, col, cube)

    def dfs_usingArray(self, board, blanks, ith, row, col, cube):
        if ith == len(blanks):
            return True
        x, y, k = blanks[ith]
        for i in range(1, 10):
            c = chr(ord('0') + i)
            if row[x][i] or col[y][i] or cube[k][i]:
                continue
            row[x][i] = True
            col[y][i] = True
            cube[k][i] = True
            board[x][y] = c
            res = self.dfs(board, blanks, ith + 1, row, col, cube)
            if res:
                return True
            board[x][y] = '.'
            row[x][i] = False
            col[y][i] = False
            cube[k][i] = False

a0 = ["....9..9.",".........","4..89...1","4.3......",".........","...5..9..","....1.7..","...4.....",".....6..."]
a1 = [".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]
a2 = []
for i in range(9):
    a2.append([])
    for j in range(9):
        a2[i].append(a0[i][j])
a = a2
for i in range(9):
    print(a[i])
print(Solution.solveSudoku(Solution(), a))
for i in range(9):
    print(a[i])