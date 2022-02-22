# 838. 推多米诺
n 张多米诺骨牌排成一行，将每张多米诺骨牌垂直竖立。在开始时，同时把一些多米诺骨牌向左或向右推。

每过一秒，倒向左边的多米诺骨牌会推动其左侧相邻的多米诺骨牌。同样地，倒向右边的多米诺骨牌也会推动竖立在其右侧的相邻多米诺骨牌。

如果一张垂直竖立的多米诺骨牌的两侧同时有多米诺骨牌倒下时，由于受力平衡， 该骨牌仍然保持不变。

就这个问题而言，我们会认为一张正在倒下的多米诺骨牌不会对其它正在倒下或已经倒下的多米诺骨牌施加额外的力。

给你一个字符串 dominoes 表示这一行多米诺骨牌的初始状态，其中：

dominoes[i] = 'L'，表示第 i 张多米诺骨牌被推向左侧，
dominoes[i] = 'R'，表示第 i 张多米诺骨牌被推向右侧，
dominoes[i] = '.'，表示没有推动第 i 张多米诺骨牌。
返回表示最终状态的字符串。

## 题解
### 最优题解
```python
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        od = ""
        while dominoes != od:
            od = dominoes
            dominoes = dominoes.replace("R.L", "T")
            dominoes = dominoes.replace(".L", "LL")
            dominoes = dominoes.replace("R.", "RR")
            dominoes = dominoes.replace("T", "R.L")
        return dominoes
```

```python
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        pre, res = (-1, 'L'), ''  # 首部的虚拟哨兵
        for i, s in enumerate(dominoes+'R'):  # 尾部的哨兵
            if s == 'L':
                if pre[1] == 'L':
                    res += 'L'*(i-pre[0])
                else:
                    div, mod = divmod((i-pre[0]-1), 2)
                    res += 'R'*div+'.'*mod+'L'*div+'L'
                pre = (i, s)
            elif s == 'R':
                if pre[1] == 'L':
                    res += '.'*(i-pre[0]-1)+'R'
                else:
                    res += 'R'*(i-pre[0])
                pre = (i, s)
        return res[:-1]  # 去掉尾部的哨兵

```

### 我的题解

```python
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dom_dict={'L':-1, 'R':1, '.':0}
        dom_dict_decode={-1:'L', 1:'R', 0:'.'}
        dom_list = [dom_dict[item] for item in dominoes]
        cnt=0
        index=0

        while cnt < (len(dom_list)-1):
            # 遇到非0数,则为推倒指令L或R
            if dom_list[cnt]!=0 and cnt<len(dom_list)-1:
                # 推进驱动
                index = cnt + dom_list[cnt]            
                # R向/L向传播判定,碰见0则一直传播
                while dom_list[index]==0:
                    print(index, cnt)
                    dom_list[index] = dom_list[cnt]
                    # 防左右越界
                    if index<=0 or index>(len(dom_list)-1):
                        break
                    # R向传播中遇到L则反传一半路程
                    if dom_list[cnt]==1 and dom_list[index+1]==-1:
                        # 计算反传的一半路程
                        offset = int((index-cnt)/2)
                        for x in range(0, offset+1):
                            dom_list[index-x] = -1
                            # 到了一半路程,反传完成
                            if (offset)%2!=0 and x==offset:
                                dom_list[index-offset] = 0
                                index+=1 # 跳过该L点防止重复处理
                        # 在R向传播中记录内圈传播推进进度
                        cnt = index
                    index+=dom_list[cnt]
                    print(dom_list)
            cnt+=1
                
        ecode_list = ''.join([dom_dict_decode[item] for item in dom_list])
        return (ecode_list)
```
