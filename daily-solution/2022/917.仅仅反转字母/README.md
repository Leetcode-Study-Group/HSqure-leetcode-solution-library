# 917. 仅仅反转字母
给你一个字符串 `s` ，根据下述规则反转字符串：

所有非英文字母保留在原有位置。
所有英文字母（小写或大写）位置反转。
返回反转后的 `s` 。

 

**示例 1：**

```python
输入：s = "ab-cd"
输出："dc-ba"
```

**示例 2：**
```python
输入：s = "a-bC-dEf-ghIj"
输出："j-Ih-gfE-dCba"
```
**示例 3：** 
```python
输入：s = "Test1ng-Leet=code-Q!"
输出："Qedo1ct-eeLg=ntse-T!"
```

**提示**

`1 <= s.length <= 100`
`s` 仅由 ASCII 值在范围 `[33, 122]` 的字符组成
`s` 不含 `'\"'` 或 `'\\'`

## 题解
### 最优题解

```python
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        p = [i for i in s if i.isalpha()]
        return ''.join([i if not i.isalpha() else p.pop() for i in s])
```

### 我的题解
**思路:**

逆序指针即可,非字母则跳过. 将所有需要反转的字母字符对应的下标(指针)存入数组`p`, 新字符串list复制原list之后,使用逆序`p`作为下标读取原list.

```python
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        orig_s = list(s)
        new_s = list(s)
        p = [i for i in range(0, len(orig_s)) if orig_s[i].isalpha()]
        for i in range(0, len(p)):
            new_s[p[i]] = orig_s[p[len(p)-1-i]]
        return ''.join(new_s)
```
