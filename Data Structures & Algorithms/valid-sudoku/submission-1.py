"""
"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # 3x3 set for boxes
        boxes = [[set(), set(), set()] for _ in range(len(board))]

        # set for each col
        coll = [set() for _ in range(len(board))]

        for row in range(len(board)):
            rset = set()
            for col in range(len(board[0])):
                # value
                val = board[row][col]

                # retrieve set for correct column
                colset = coll[col]

                # CHECK ROWS AND COLUMN, AND BOXES
                if val != ".":
                    # ROWS
                    if val not in rset:
                        rset.add(val)
                    else:
                        return False # duplicate number in row

                    # COLS
                    if val not in colset:
                        colset.add(val)
                    else:
                        return False

                    br, bc = row // 3, col // 3
                    if val not in boxes[br][bc]:
                        boxes[br][bc].add(val)
                    else:
                        return False


        return True
