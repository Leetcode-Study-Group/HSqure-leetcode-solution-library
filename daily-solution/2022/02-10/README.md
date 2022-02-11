# 1447. 最简分数

## 问题:
给你一个整数 `n` ，请你返回所有 0 到 1 之间（不包括 0 和 1）满足分母小于等于  `n` 的**最简**分数 。分数可以以**任意**顺序返回。

 
**示例 1：**
```shell
输入：n = 2
输出：["1/2"]
解释："1/2" 是唯一一个分母小于等于 2 的最简分数。
```
**示例 2：**
```shell
输入：n = 3
输出：["1/2","1/3","2/3"]
```
**示例 3：**
```shell
输入：n = 4
输出：["1/2","1/3","1/4","2/3","3/4"]
解释："2/4" 不是最简分数，因为它可以化简为 "1/2" 。
```
**示例 4：**
```shell
输入：n = 1
输出：[]
```

**提示：**

```
1 <= n <= 100
```


## 题解
思路:遍历3轮:分母1轮,分子1轮,检查是否可约(叔叔我们不约)1轮,一旦查出可约,直接把这轮丢弃,反正约分后必有重复.

```python
class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        fractions_list=[]
        for nn in range(2, n+1):
            for i in range(1, nn):
                dividable_tag=False
                # checking
                for elem in range(2,i+1):
                    if (i%elem==0 and nn%elem==0):
                        dividable_tag=True
                if not dividable_tag:
                    fractions_list.append(f'{i}/{nn}')
        return fractions_list
```
