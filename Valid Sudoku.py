class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        '''
        Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated. 
        '''
        row = [set() for i in range(9)]
        col = [set() for i in range(9)]
        cube = [set() for i in range(9)]
        for i in range(9):
            for j in range(9):
                x = board[i][j]
                k = i // 3 * 3 + j // 3
                if x == '.':
                    continue
                if x in row[i] or x in col[j] or x in cube[k]:
                    return False
                row[i].add(x)
                col[j].add(x)
                cube[k].add(x)
        return True

a0 = ["....9..9.",".........","4..89...1","4.3......",".........","...5..9..","....1.7..","...4.....",".....6..."]
a1 = [".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]

a = a1
for i in range(9):
    print(a[i])
print(Solution.isValidSudoku(Solution(), a))