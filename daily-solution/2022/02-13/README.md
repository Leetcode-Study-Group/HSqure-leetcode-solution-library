# 1189. “气球” 的最大数量
给你一个字符串 text，你需要使用 text 中的字母来拼凑尽可能多的单词 "balloon"（气球）。
字符串 text 中的每个字母最多只能被使用一次。请你返回最多可以拼凑出多少个单词 "balloon"。

 

**示例 1：**
```shell
输入：text = "nlaebolko"
输出：1
```
**示例 2：**
```shell
输入：text = "loonbalxballpoon"
输出：2
```
**示例 3：**
```shell
输入：text = "leetcode"
输出：0
```

提示：
```
1 <= text.length <= 10^4
text 全部由小写英文字母组成
```

## 最优题解
**思路:**
将输入的`text`中包含的`balon`都遍历并通过`Counter`函数存到字典中,将需要用两次的字母除以`2`,此时其中最少的数字数量即为最多能用来拼成词`balloon`的数量.此外还要保证每个字母种类都有(字典`len`为`5`)

```python
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cnt = Counter(ch for ch in text if ch in "balon")
        cnt['l']=cnt['l']//2
        cnt['o']=cnt['o']//2
        
        return min(cnt.values()) if len(cnt)==5 else 0
```

## 我的题解
```python
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon_list = ['b', 'a', 'l', 'l', 'o', 'o', 'n']
        text_list=[]
        flag=True
        cnt=0
        for i in range(0,len(text)):
            text_list.append(text[i])
        
        while flag:
            for key in balloon_list:
                if key in text_list:
                    text_list.remove(key)
                else:
                    flag=False
                    break
                if key=='n':
                    cnt+=1

        return cnt

```
