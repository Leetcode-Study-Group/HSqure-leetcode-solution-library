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
### 我的题解

```python
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        dom_dict={'L':-1, 'R':1, '.':0}
        dom_dict_decode={-1:'L', 1:'R', 0:'.'}
        dom_list = [dom_dict[item] for item in dominoes]
        flag=True
        for cnt, i in enumerate(dom_list): 
            if i!=0 and cnt<len(dom_list)-1:
                # 首次赋值
                if flag:
                    index = cnt
                    flag=False                
                if index<0 or index>(len(dom_list)-3):
                    break
                index+=i
                print(index)
                # R传播判定
                while dom_list[index]==0:
                    # 防越界
                    if index<0 or index>(len(dom_list)-3):
                        break
                    dom_list[index] = i
                    # R遇到L反弹一半路程 
                    offset = int((index-cnt)/2)
                    if i==1 and dom_list[index+1]==-1:
                        for x in range(0, offset):
                            dom_list[index-x] = -i
                            if (offset)%2!=0:
                                dom_list[index-offset] = 0
    
                    index+=i
                
                print(dom_list)

        ecode_list = ''.join([dom_dict_decode[item] for item in dom_list])
        print('"'+ecode_list+'"')
```
