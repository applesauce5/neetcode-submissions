"""
BFS from each 0
> take the min at each step of the bfs
> -1 are walls

"""

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        def bfs(g: List[List[int]], q, seen):
            while q:
                row, col, ct = q.pop(0)
                seen.add((row,col))
                #print(row, col)
                g[row][col] = min(ct, g[row][col])

                if 0 < row and g[row-1][col] not in [-1, 0] and (row-1,col) not in seen:
                    q.append((row-1, col, ct+1))

                if row < len(g) - 1 and g[row+1][col] not in [-1, 0] and (row+1,col) not in seen:
                    #print("append",row+1, col)
                    q.append((row+1, col, ct+1))

                if 0 < col and g[row][col-1] not in [-1, 0] and (row,col-1) not in seen:
                    q.append((row, col-1, ct+1))
                
                if col < len(g[0]) - 1 and g[row][col+1] not in [-1, 0] and (row,col+1) not in seen:
                    q.append((row, col+1, ct+1))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    seen = set()
                    q = list()
                    #print("---")
                    q.append((i,j, 0))
                    bfs(grid, q, seen)
