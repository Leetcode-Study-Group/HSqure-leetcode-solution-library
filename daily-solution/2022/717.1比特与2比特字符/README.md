# 717. 1比特与2比特字符

有两种特殊字符：

- 第一种字符可以用一个比特 `0` 来表示
- 第二种字符可以用两个比特(`10` 或 `11`)来表示、
给定一个以 `0` 结尾的二进制数组 `bits` ，如果最后一个字符必须是一位字符，则返回 `true` 。

 

**示例 1:**
```python
输入: bits = [1, 0, 0]
输出: true
解释: 唯一的编码方式是一个两比特字符和一个一比特字符。
所以最后一个字符是一比特字符。
```

**示例 2:**
```python
输入: bits = [1, 1, 1, 0]
输出: false
解释: 唯一的编码方式是两比特字符和两比特字符。
所以最后一个字符不是一比特字符。
```

**提示:**

- `1 <= bits.length <= 1000`
- `bits[i] == 0 or 1`

## 题解

### 最优题解
```python

```

### 我的题解
**思路**

遇到`1`则说明这个必为双数字字符，则`cnt`多加一个1跳过下一个下标，因此`cnt`不连续，值为每个(单/双)字符的首个数字的下标，当它的值等于`list`长度时，则说明最后一个碰上没跳过的单数字字符了。
```python
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        cnt = -1
        while not cnt+1 >= len(bits):
            cnt+=1
            if cnt+1 == len(bits):
                return True
            # 有1则跳过一个下标
            if bits[cnt] == 1:
                cnt+=1
            
        return False
```
