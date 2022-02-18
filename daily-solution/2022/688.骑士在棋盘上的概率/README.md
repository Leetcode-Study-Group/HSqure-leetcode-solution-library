# 688. 骑士在棋盘上的概率

在一个 `n x n` 的国际象棋棋盘上，一个骑士从单元格 `(row, column)` 开始，并尝试进行 `k` 次移动。行和列是 **从 0 开始** 的，所以左上单元格是 `(0,0)` ，右下单元格是 `(n - 1, n - 1)` 。

## 背景信息
象棋骑士有8种可能的走法，如下图所示。每次移动在基本方向上是两个单元格，然后在正交方向上是一个单元格。

![移动规则](./../../../document_source/knight.png)

每次骑士要移动时，它都会随机从8种可能的移动中选择一种(即使棋子会离开棋盘)，然后移动到那里。

骑士继续移动，直到它走了 k 步或离开了棋盘。

返回 ***骑士在棋盘停止移动后仍留在棋盘上的概率*** 。

 

**示例 1：**
```python
输入: n = 3, k = 2, row = 0, column = 0
输出: 0.0625
解释: 有两步(到(1,2)，(2,1))可以让骑士留在棋盘上。
在每一个位置上，也有两种移动可以让骑士留在棋盘上。
骑士留在棋盘上的总概率是0.0625。
```

**示例 2：**
```python
输入: n = 1, k = 0, row = 0, column = 0
输出: 1.00000
```

提示:

- `1 <= n <= 25`
- `0 <= k <= 100`
- `0 <= row, column <= n`


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

### 官方题解

**方法一：动态规划**
**思路**

一个骑士有 88 种可能的走法，骑士会从中以等概率随机选择一种。部分走法可能会让骑士离开棋盘，另外的走法则会让骑士移动到棋盘的其他位置，并且剩余的移动次数会减少 11。

定义 \textit{dp}[\textit{step}][i][j]dp[step][i][j] 表示骑士从棋盘上的点 (i, j)(i,j) 出发，走了 \textit{step}step 步时仍然留在棋盘上的概率。特别地，当点 (i, j)(i,j) 不在棋盘上时，\textit{dp}[\textit{step}][i][j] = 0dp[step][i][j]=0；当点 (i, j)(i,j) 在棋盘上且 \textit{step} = 0step=0 时，\textit{dp}[\textit{step}][i][j] = 1dp[step][i][j]=1。对于其他情况，\textit{dp}[\textit{step}][i][j] = \dfrac{1}{8} \times \sum\limits_{\textit{di}, \textit{dj}} \textit{dp}[\textit{step}-1][i+\textit{di}][j+\textit{dj}]dp[step][i][j]= 
8
1
​	
 × 
di,dj
∑
​	
 dp[step−1][i+di][j+dj]。其中 (\textit{di}, \textit{dj})(di,dj) 表示走法对坐标的偏移量，具体为 (-2, -1),(-2,1),(2,-1),(2,1),(-1,-2),(-1,2),(1,-2),(1,2)(−2,−1),(−2,1),(2,−1),(2,1),(−1,−2),(−1,2),(1,−2),(1,2) 共 88 种。

**复杂度分析**

时间复杂度：O(k \times n ^ 2)O(k×n 
2
 )。状态数一共有 O(k \times n ^ 2)O(k×n 
2
 )，每次转移需要考虑 88 种可能的走法，消耗 O(1)O(1) 的时间复杂度，总体的时间复杂度是 O(k \times n ^ 2)O(k×n 
2
 )。

空间复杂度：O(k \times n ^ 2)O(k×n 
2
 )。状态数一共有 O(k \times n ^ 2)O(k×n 
2
 )，用一个数组来保存。注意到每一步的状态只由前一步决定，空间复杂度可以优化到 O(n ^ 2)O(n 
2
 )。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/knight-probability-in-chessboard/solution/qi-shi-zai-qi-pan-shang-de-gai-lu-by-lee-2qhk/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

```python
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dp = [[[0] * n for _ in range(n)] for _ in range(k + 1)]
        for step in range(k + 1):
            for i in range(n):
                for j in range(n):
                    if step == 0:
                        dp[step][i][j] = 1
                    else:
                        for di, dj in ((-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)):
                            ni, nj = i + di, j + dj
                            if 0 <= ni < n and 0 <= nj < n:
                                dp[step][i][j] += dp[step - 1][ni][nj] / 8
        return dp[k][row][column]

```

---

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
