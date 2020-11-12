"""
You are given a 2d grid of `"1"`s and `"0"`s that represents a "map". The
`"1"`s represent land and the `"0"s` represent water.

You need to write a function that, given a "map" as an argument, counts the
number of islands. Islands are defined as adjacent pieces of land that are
connected horizontally or vertically. You can also assume that the edges of the
map are surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""
from collections import deque

def numIslands(grid):
    # Your code here
    num_islands = 0
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == '1':
                num_islands += 1
                stack = [(x, y)]
                grid[x][y] = '0'

                while stack:
                    i, j = stack.pop()
                    if i + 1 < len(grid) and grid[i + 1][j] == '1':
                        grid[i + 1][j] = '0'
                        stack.append((i + 1, j))
                    if j + 1 < len(grid[i]) and grid[i][j + 1] == '1':
                        grid[i][j + 1] = '0'
                        stack.append((i, j + 1))
    return num_islands                    
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
# I think this breaks because it doesn't check left (or up for that matter)
print(numIslands(grid))
print(numIslands([['0','1'],['1','1']]))
# yup