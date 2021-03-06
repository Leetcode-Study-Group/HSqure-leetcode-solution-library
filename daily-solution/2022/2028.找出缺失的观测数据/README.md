# 2028. 找出缺失的观测数据
现有一份 `n + m` 次投掷单个 六面 骰子的观测数据，骰子的每个面从 `1` 到 `6` 编号。观测数据中缺失了 `n` 份，你手上只拿到剩余 `m` 次投掷的数据。幸好你有之前计算过的这 `n + m` 次投掷数据的 **平均值** 。

给你一个长度为 `m` 的整数数组 `rolls` ，其中 `rolls[i]` 是第 i 次观测的值。同时给你两个整数 `mean` 和 `n` 。

返回一个长度为 `n` 的数组，包含所有缺失的观测数据，且满足这 `n + m` 次投掷的 **平均值** 是 `mean` 。如果存在多组符合要求的答案，只需要返回其中任意一组即可。如果不存在答案，返回一个空数组。

`k` 个数字的 **平均值** 为这些数字求和后再除以 k 。

注意 `mean` 是一个整数，所以 `n + m` 次投掷的总和需要被 n + m 整除。

 

**示例 1：**
```python
输入：rolls = [3,2,4,3], mean = 4, n = 2
输出：[6,6]
解释：所有 n + m 次投掷的平均值是 (3 + 2 + 4 + 3 + 6 + 6) / 6 = 4 。
```
**示例 2：**
```python
输入：rolls = [1,5,6], mean = 3, n = 4
输出：[2,3,2,2]
解释：所有 n + m 次投掷的平均值是 (1 + 5 + 6 + 2 + 3 + 2 + 2) / 7 = 3 。
```
**示例 3：**
```python
输入：rolls = [1,2,3,4], mean = 6, n = 4
输出：[]
解释：无论丢失的 4 次数据是什么，平均值都不可能是 6 。
```
**示例 4：**
```python
输入：rolls = [1], mean = 3, n = 1
输出：[5]
解释：所有 n + m 次投掷的平均值是 (1 + 5) / 2 = 3 。
```

提示：

- `m == rolls.length`
- `1 <= n, m <= 105`
- `1 <= rolls[i], mean <= 6`

## 题解
难点在于剩下的值的分配方式.主要有以下两种构造方式:
### 方法一
**思路:** 构造方式为优先填满能填满的部分.
```python

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        # 缺失部分数据值之和 = (总数据个数 * 总数据值均值) - 已知数据值之和
        missing_sum = (len(rolls)+n) * mean - sum(rolls)
        # 不符合骰子表达范围则返回空
        if missing_sum > n * 6 or missing_sum < n:
            return []
        else:
            """   
            均值分配方式: 水倒冰格.将这部分的和(missing_sum)逐个填入6容量的区间,
                        填满则下一个,直到值用完,格子数为n,空格子初始值为1
            """    
            # 商(填满的格子数), 余数 
            num, reminder = divmod(missing_sum-n, 5)
            # 初始填1
            missing_list = [1] * n
            # 填满部分
            missing_list[:num] = [6] * num
            # 余出部分
            missing_list[-1] += reminder
            return missing_list
```

---

### 方法二
**思路:** 构造方式为先平均分配,把余下的数再分摊．
```python

class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        missingSum = mean * (n + len(rolls)) - sum(rolls)
        if not n <= missingSum <= n * 6:
            return []
        quotient, remainder = divmod(missingSum, n)
        return [quotient + 1] * remainder + [quotient] * (n - remainder)

```
**复杂度分析**


- **时间复杂度**：`O(n + m)`，其中 `n` 是缺失的观测数据个数，`m` 是数组 `rolls` 的长度，即已知的观测数据个数。需要 `O(m)`的时间计算缺失的观测数据之和，需要 `O(n)` 的时间构造答案。

- **空间复杂度**：`O(1)`。除了返回值以外，使用的额外空间为 `O(1)`。
