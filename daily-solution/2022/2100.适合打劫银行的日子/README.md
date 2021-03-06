# 2100. 适合打劫银行的日子
你和一群强盗准备打劫银行。给你一个下标从 `0` 开始的整数数组 `security` ，其中 `security[i]` 是第 `i` 天执勤警卫的数量。日子从 `0` 开始编号。同时给你一个整数 `time `。
如果第 `i` 天满足以下所有条件，我们称它为一个适合打劫银行的日子：


- 第 `i` 天前和后都分别至少有 `time` 天。
- 第 `i` 天前连续 `time` 天警卫数目都是 **非递增** 的。
- 第 `i` 天后连续 `time` 天警卫数目都是 **非递减** 的。

更正式的，第 `i` 天是一个合适打劫银行的日子当且仅当：
```python
security[i - time] >= security[i - time + 1] >= ... >= security[i] <= ... <= security[i + time - 1] <= security[i + time]
```
请你返回一个数组，包含 **所有** 适合打劫银行的日子（下标从 `0` 开始）。返回的日子可以 **任意** 顺序排列。

 

**示例 1：**
```python
输入：security = [5,3,3,3,5,6,2], time = 2
输出：[2,3]
解释：
第 2 天，我们有 security[0] >= security[1] >= security[2] <= security[3] <= security[4] 。
第 3 天，我们有 security[1] >= security[2] >= security[3] <= security[4] <= security[5] 。
没有其他日子符合这个条件，所以日子 2 和 3 是适合打劫银行的日子。
```
**示例 2：**
```python
输入：security = [1,1,1,1,1], time = 0
输出：[0,1,2,3,4]
解释：
因为 time 等于 0 ，所以每一天都是适合打劫银行的日子，所以返回每一天。
```
**示例 3：**
```python
输入：security = [1,2,3,4,5,6], time = 2
输出：[]
解释：
没有任何一天的前 2 天警卫数目是非递增的。
所以没有适合打劫银行的日子，返回空数组。
```
**示例 4：**
```python
输入：security = [1], time = 5
输出：[]
解释：
没有日子前面和后面有 5 天时间。
所以没有适合打劫银行的日子，返回空数组。
```

**提示：**

- `1 <= security.length <= 105`
- `0 <= security[i], time <= 105`

---

## 题解
### 最优题解
**思路**

**前缀和**思想: 

前缀和
为了方便，我们令 nn 为 securitysecurity 长度。

根据题目对「适合打劫银行的日子」的定义，首先我们可以确定答案落在 [time, n - time) 范围内，另外规定了「适合打劫银行的日子」左右侧需要满足「非递增」和「非递减」的性质。

首先我们可以预处理 g 数组，g[i]g[i] 代表当前时间 security[i] 与前一时间 security[i - 1]的大小关系，当 security[i] > security[i - 1]security[i]>security[i−1] 时有 g[i] = 1g[i]=1，当 security[i] < security[i - 1]security[i]<security[i−1] 时有 g[i] = -1g[i]=−1，否则 g[i] = 0g[i]=0，另外我们特别的有 g[0] = 0g[0]=0 的边界情况。

然后我们对 g 应用「前缀和」思想：使用 a 数组记录前缀 11 的数量，使用 b 数组记录前缀 -1−1 的数量。

最终，如果 ii 为「适合打劫银行的日子」，那么满足 time <= i < n - timetime<=i<n−time，且满足 (i - time, i](i−time,i] 范围前缀 11 数量为 00，(i, i + time](i,i+time] 范围前缀 -1−1 数量为 00。

```python

```

### 我的题解
```python
class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        gdlist=[]
        window=[1,-1]
        if len(security) < 2 * time + 1:
            return gdlist
        for i in range(time, len(security)-time):
            good_day_sign = True
            for offset in range(0, time):
                # 满足条件则将当前i计入goodday list
                if (security[i-offset] * window[0] + security[i-(offset+1)] * window[1] <=0) and \
                    (security[i+offset] * window[0] + security[i+(offset+1)] * window[1] <=0):
                   # 该点满足条件
                    sign = True
                else:
                    sign = False
                # 该轮(i的time范围内)所有点是否满足条件
                good_day_sign = good_day_sign & sign
                # print(i,offset,sign,good_day_sign)
            # print(good_day_sign)
            if good_day_sign:
                gdlist.append(i)

        return gdlist
```
