"""
Lands are blocks connected up, down, left, right

BFS or DFS each island you encounter
- when done, turn each land into water(0)

Return the number of BFS/DFS you have done
"""


def bfs(i,j,grid):
    grid[i][j] = "0"
    dirs = [(1,0), (0,1), (-1,0), (0,-1)]

    for mrow, mcol in dirs:
        if 0 <= (i + mrow) < len(grid): # row boundary
            if 0 <= (j + mcol) < len(grid[0]): # column boundary
                if grid[i + mrow][j + mcol] == "1":
                    bfs(i + mrow, j + mcol, grid)

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ct = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    ct += 1
                    bfs(i,j,grid)
                         
        return ct
        