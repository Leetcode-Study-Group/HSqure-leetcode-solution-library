# 693. 交替位二进制数
给定一个正整数，检查它的二进制表示是否总是 0、1 交替出现：换句话说，就是二进制表示中相邻两位的数字永不相同。

 

示例 1：
```python
输入：n = 5
输出：true
解释：5 的二进制表示是：101
```
示例 2：
```python
输入：n = 7
输出：false
解释：7 的二进制表示是：111.
```
示例 3：
```python
输入：n = 11
输出：false
解释：11 的二进制表示是：1011.
``` 

提示：

- `1 <= n <= 231 - 1`

## 题解
**异或**方法的重点在于：**异或**出来后的`0b1111...`怎么转换为方便判别的的标志。

**1.**
```python
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        a = n ^ (n >> 1)
        return a & (a + 1) == 0 # 将0b1111...转换为0方便判断
```
**2.**
```python
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        return not ('11' in bin(n) or '00' in bin(n))
```
**我的题解**

```python
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        return bin(n^(n>>1)).count('0')==1
```
