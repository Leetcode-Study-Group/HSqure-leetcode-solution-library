# 1020. 飞地的数量
`Date 2/12`


给你一个大小为 `m x n` 的二进制矩阵 `grid` ，其中 `0` 表示一个海洋单元格、1 表示一个陆地单元格。
一次 移动 是指从一个陆地单元格走到另一个相邻（上、下、左、右）的陆地单元格或跨过 grid 的边界。
返回网格中 无法 在任意次数的移动中离开网格边界的陆地单元格的数量。

 

**示例 1：**

```shell
输入：grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
输出：3
解释：有三个 1 被 0 包围。一个 1 没有被包围，因为它在边界上。
```

**示例 2：**

```shell
输入：grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
输出：0
解释：所有 1 都在边界上或可以到达边界。
 ```

提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 500
grid[i][j] 的值为 0 或 1


## 题解
本题中DFS和BFS只是修改元素值的手段，都可以用。相比之下DFS用的内存稍微多一些，时间都差不多

### 方法一：DFS

执行用时：80 ms, 在所有 Python3 提交中击败了84.99%的用户

内存消耗：17 MB, 在所有 Python3 提交中击败了13.17%的用户
```python
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            grid[i][j] = 0
            for x, y in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                if 0 <= x < m and 0 <= y < n and grid[x][y]:
                    dfs(x, y)                    

        m, n = len(grid), len(grid[0])
        for i in range(m):
            if grid[i][0] == 1:    dfs(i, 0)
            if grid[i][n-1] == 1:  dfs(i, n-1)   
        for j in range(n):
            if grid[0][j] == 1:    dfs(0, j)
            if grid[m-1][j] == 1:  dfs(m-1, j)
                
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]: ans += 1
        return ans
```
### 方法二：BFS

执行用时：76 ms, 在所有 Python3 提交中击败了90.53%的用户

内存消耗：15.9 MB, 在所有 Python3 提交中击败了71.83%的用户
```python
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def bfs(i, j):
            grid[i][j] = 0
            Q = deque([[i, j]])
            while Q:
                i, j = Q.popleft()
                for x, y in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                    if 0 <= x < m and 0 <= y < n and grid[x][y]:
                        grid[x][y] = 0
                        Q.append([x, y])                  

        m, n = len(grid), len(grid[0])
        for i in range(m):
            if grid[i][0] == 1:    bfs(i, 0)
            if grid[i][n-1] == 1:  bfs(i, n-1)   
        for j in range(n):
            if grid[0][j] == 1:    bfs(0, j)
            if grid[m-1][j] == 1:  bfs(m-1, j)
                
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]: ans += 1
        return ans
```
