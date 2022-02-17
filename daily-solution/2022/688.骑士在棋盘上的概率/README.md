# 688. 骑士在棋盘上的概率

在一个 `n x n` 的国际象棋棋盘上，一个骑士从单元格 `(row, column)` 开始，并尝试进行 `k` 次移动。行和列是 **从 0 开始** 的，所以左上单元格是 `(0,0)` ，右下单元格是 `(n - 1, n - 1)` 。

## 背景信息
象棋骑士有8种可能的走法，如下图所示。每次移动在基本方向上是两个单元格，然后在正交方向上是一个单元格。



每次骑士要移动时，它都会随机从8种可能的移动中选择一种(即使棋子会离开棋盘)，然后移动到那里。

骑士继续移动，直到它走了 k 步或离开了棋盘。

返回 骑士在棋盘停止移动后仍留在棋盘上的概率 。

 

示例 1：

输入: n = 3, k = 2, row = 0, column = 0
输出: 0.0625
解释: 有两步(到(1,2)，(2,1))可以让骑士留在棋盘上。
在每一个位置上，也有两种移动可以让骑士留在棋盘上。
骑士留在棋盘上的总概率是0.0625。
示例 2：

输入: n = 1, k = 0, row = 0, column = 0
输出: 1.00000
 

提示:

1 <= n <= 25
0 <= k <= 100
0 <= row, column <= n

## 题解
### 最优题解
和[576. 出界的路径数](https://leetcode-cn.com/problems/out-of-boundary-paths/)很类似，都是根据当前的位置推断下一步的位置

首先创建一个棋盘`cur_pos`，将起始位置设置为`1`，表示有1步可以到达该位置

然后开始循环`k`次，每次都创建一个新的棋盘`new_pos`，表示最后棋盘上的各点有多少条路径能到达

然后遍历`cur_pos`，如果`cur_pos[i][j]`值不为`0`，则判断从该点出发到达的8个点`(x,y)`是否在棋盘内，如果在就将`new_pos[x][y]`的值加上`cur_pos[i][j]`处的值（有`cur_pos[i][j]`条线路可以到达该处）

遍历结束后，遍历`cur_pos`，计算所有能留在棋盘上的路径数`cur_total_pos`，因为总共有`8 ** k`条路径，所以概率为 `cur_total_pos / (8 ** k)`

```python
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        cur_pos = [[0] * n for _ in range(n)]
        cur_pos[row][column] = 1
        for _ in range(k):
            new_pos = [[0] * n for _ in range(n)]   #表示走完该步以后的情况
            for i in range(n):
                for j in range(n):
                    if cur_pos[i][j]:  #尝试往八个方向走
                        for x, y in [(i-2,j-1),(i-1,j-2),(i+1,j-2),(i+2,j-1),(i-2,j+1),(i-1,j+2),(i+1,j+2),(i+2,j+1)]:
                            if 0 <= x < n and 0 <= y < n:
                                new_pos[x][y] += cur_pos[i][j]  #更新new_pos上的路径数量
            cur_pos = new_pos  #更新cur_pos

        #计算所有可能的路径数
        cur_total_pos = 0
        for i in range(n):
            for j in range(n):
                cur_total_pos += cur_pos[i][j]
                    
        return cur_total_pos / (8 ** k)

```
### 我的题解

```python
class Solution:
    mov_around = [[1,2],[2,1], [2,-1],[1,-2], [-1,-2],[-2,-1], [-2,1],[-1,2]]

    def move_around(axis):
        # 遍历所有方向
        for i in range(0, 8):
            r_axis = kngi_axis[0] + mov_around[i][0]
            c_axis = kngi_axis[1] + mov_around[i][1]
            if (r_axis < 0) or (c_axis < 0):
                return False 
            else:
    
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        memo = {}
        moves = ((-1, -2), (-2, -1),(-2, 1), (-1, 2),(1, -2), (2, -1),(2, 1), (1, 2))
        def dfs(K, r, c):
            if r < 0 or c < 0 or r >= N or c >= N:
                return 0
            if K == 0:
                return 1
            if (K, r, c) in memo:
                return memo[(K, r, c)]
            p = 0
            for move in moves:
                p += dfs(K-1, r+move[0], c+move[1])
            p /= 8.0
            memo[(K, r, c)] = p
            return p
        return dfs(K, r, c)

        # 初始位置
        kngi_axis = [row, column]

        for step in range(1, k+1):
```
