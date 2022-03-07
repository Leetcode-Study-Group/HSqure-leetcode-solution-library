# 504. 七进制数
给定一个整数 num，将其转化为 7 进制，并以字符串形式输出。

 

示例 1:

输入: num = 100
输出: "202"
示例 2:

输入: num = -7
输出: "-10"

# 题解
## 我的题解
```python
class Solution:
    def convertToBase7(self, num: int) -> str:
        minus_flag=False
        divider=7
        if num<0:
            minus_flag=True
            num = - num
        num_list=[] if num is not 0 else ['0']
        while(num!=0):
            num_list.append(str(num%divider))
            num=num//divider
        num_list.reverse()
        return '-'+''.join(num_list) if minus_flag else ''.join(num_list)
```
