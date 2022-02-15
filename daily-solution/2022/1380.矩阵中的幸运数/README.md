# 1380. 矩阵中的幸运数
给你一个 `m * n` 的矩阵，矩阵中的数字 **各不相同** 。请你按 **任意** 顺序返回矩阵中的所有幸运数。
幸运数是指矩阵中满足同时下列两个条件的元素：

- 在同一行的所有元素中最小
- 在同一列的所有元素中最大
 

**示例 1：**

输入：matrix = [[3,7,8],[9,11,13],[15,16,17]]
输出：[15]
解释：15 是唯一的幸运数，因为它是其所在行中的最小值，也是所在列中的最大值。

**示例 2：**

输入：matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
输出：[12]
解释：12 是唯一的幸运数，因为它是其所在行中的最小值，也是所在列中的最大值。
示例 3：

输入：matrix = [[7,8],[1,2]]
输出：[7]
 

提示：

- `m == mat.length`
- `n == mat[i].length`
- `1 <= n, m <= 50`
- `1 <= matrix[i][j] <= 10^5`
- 矩阵中的所有元素都是不同的

## 题解

### 最优题解
思路:行最小和列最大分别保存到列表里进行比对,相同则输出

```python
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        rowmin = [min(i) for i in matrix]
        colmin = [max(i) for i in zip(*matrix)]
        return [i for i in rowmin if i in colmin]
```

### 我的题解
思路:先找行最小,此时和该位置所在行的最大的进行比对,相同则输出
```python
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        lucky_list=[]
        for r in matrix:
            min_r = min(r)
            c_list = [rr[r.index(min_r)] for rr in matrix]
            if max(c_list) == min_r:
                lucky_list.append(min_r)

        return lucky_list
```
