# 6. Z 字形变换
将一个给定字符串 `s` 根据给定的行数 `numRows` ，以从上往下、从左到右进行 **Z 字形排列**。
比如输入字符串为 `PAYPALISHIRING` ,行数为 `3` 时，排列如下：
```python
P   A   H   N
A P L S I I G
Y   I   R
```
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如`PAHNAPLSIIGYIR`。

请你实现这个将字符串进行指定行数变换的函数：
```python
string convert(string s, int numRows);
```
 

**示例 1：**
```python
输入：s = "PAYPALISHIRING", numRows = 3
输出："PAHNAPLSIIGYIR"
```

**示例 2：**
```python
输入：s = "PAYPALISHIRING", numRows = 4
输出："PINALSIGYAHRPI"
解释：
P     I    N
A   L S  I G
Y A   H R
P     I
```

**示例 3：**
```python
输入：s = "A", numRows = 1
输出："A"
```

提示：
- `1 <= s.length <= 1000`
- `s` 由英文字母（小写和大写）、`,` 和 `.` 组成
- `1 <= numRows <= 1000`

## 题解
### 最优题解
```python
```

### 我的题解
```python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        # 余数
        remainder = (len(s) - 1) % (numRows-1)
        # 余行
        line_rem = int(((len(s) - 1 - remainder) / (numRows-1))%2)
        # 行最大值
        nmax = int(((len(s) - 1 - remainder) / (numRows-1))//2+1)
        remainder = numRows -1 - remainder if line_rem else remainder
        new_str=[]
        for c in range(0, numRows):
            for n in range(0, nmax):
                # 特殊情况处理
                if c==0 or c==numRows-1 or n==nmax-1:
                    # 在最后一列时
                    if n==nmax-1:
                        # 如果补斜                        
                        if line_rem:
                            new_str.append(s[n*(2*(numRows-1))+c])
                            if remainder<1 and c!=numRows-1:
                                new_str.append(s[2*(numRows-1)*(n+1)-c])
                        # 如果补竖
                        else:
                            if remainder>=0:
                                new_str.append(s[n*(2*(numRows-1))+c])
                    else:
                        new_str.append(s[n*(2*(numRows-1))+c])
                else:
                    new_str.append(s[n*(2*(numRows-1))+c])
                    new_str.append(s[2*(numRows-1)*(n+1)-c])
            remainder -= 1
        return ''.join(new_str)
```
