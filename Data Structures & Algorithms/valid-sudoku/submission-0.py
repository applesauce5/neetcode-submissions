"""
3 checks
column row box

Worst case:
 - go through every row and validate uniques
 - go through every column and validate uniquenes

> identify center of each box and verify uniqueness
  - checking all squares of the box
"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        l = len(board)

        # Check every row
        for i in range(l):
            _s = set()
            for j in range(l):
                value = board[i][j]
                if value not in _s:
                    if value != ".":
                        _s.add(value)
                else:
                    return False

        # Check every column
        for i in range(l):
            _s = set()
            for j in range(l):
                value = board[j][i]
                if value not in _s:
                    if value != ".":
                        _s.add(value)
                else:
                    
                    return False

        # check every square
        coordinates = [
            (1,1), (4,1), (7,1), 
            (1,4), (4,4), (7,4),
            (1,7), (4,7), (7,7)
         ]

        combos = [
            (-1,-1), (-1,0), (-1,1),
            (0,-1), (0,0), (0, 1),
            (1,-1), (1,0), (1,1)
        ]

        for row, col in coordinates:
            _s = set()
            for i, j in combos:
                num = board[row + i][col + j]
                if num not in _s:
                    if num != ".":
                        _s.add(num)
                else:
                   
                    return False


        return True    