# 653. 两数之和 IV - 输入 BST
给定一个二叉搜索树 root 和一个目标结果 k，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。


**示例 1：**

```
输入: root = [5,3,6,2,4,null,7], k = 9
输出: true
```
**示例 2：**
```

输入: root = [5,3,6,2,4,null,7], k = 28
输出: false
``` 

**提示:**

- 二叉树的节点个数的范围是  `[1, 104]`.
- `-104 <= Node.val <= 104`
- `root` 为二叉搜索树
- `-105 <= k <= 105`

## 题解
### 最优题解
#### 方法一：深度优先搜索 + 哈希表
**思路和算法**


我们可以使用深度优先搜索的方式遍历整棵树，用哈希表记录遍历过的节点的值。

对于一个值为 `x` 的节点，我们检查哈希表中是否存在 `k - x` 即可。如果存在对应的元素，那么我们就可以在该树上找到两个节点的和为 `k`； 否则，我们将 `x` 放入到哈希表中。

如果遍历完整棵树都不存在对应的元素，那么该树上不存在两个和为 `k` 的节点。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.s = set()

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False
        if k - root.val in self.s:
            return True
        self.s.add(root.val)
        return self.findTarget(root.left, k) or self.findTarget(root.right, k)

```
#### 复杂度分析

- 时间复杂度：`O(n)`，其中 `n` 为二叉搜索树的大小。我们需要遍历整棵树一次。
- 空间复杂度：`O(n)`，其中 `n` 为二叉搜索树的大小。主要为哈希表的开销，最坏情况下我们需要将每个节点加入哈希表一次。
