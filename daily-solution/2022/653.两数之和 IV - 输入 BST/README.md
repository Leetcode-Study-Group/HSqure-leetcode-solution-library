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
### 方法一：深度优先搜索 + 哈希表
**思路和算法**

我们可以使用深度优先搜索的方式遍历整棵树，用哈希表记录遍历过的节点的值。

对于一个值为 `x` 的节点，我们检查哈希表中是否存在 `k - x` 即可。如果存在对应的元素，那么我们就可以在该树上找到两个节点的和为 `k`； 否则，我们将 `x` 放入到哈希表中。

如果遍历完整棵树都不存在对应的元素，那么该树上不存在两个和为 `k` 的节点。

**代码**

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
### 复杂度分析

- 时间复杂度：`O(n)`，其中 `n` 为二叉搜索树的大小。我们需要遍历整棵树一次。
- 空间复杂度：`O(n)`，其中 `n` 为二叉搜索树的大小。主要为哈希表的开销，最坏情况下我们需要将每个节点加入哈希表一次。

---

### 方法二：广度优先搜索 + 哈希表
**思路和算法**

我们可以使用广度优先搜索的方式遍历整棵树，用哈希表记录遍历过的节点的值。

具体地，我们首先创建一个哈希表和一个队列，将根节点加入队列中，然后执行以下步骤：

从队列中取出队头，假设其值为 `x`；
检查哈希表中是否存在 `k - x`，如果存在，返回 `True`；
否则，将该节点的左右的非空子节点加入队尾；
重复以上步骤，直到队列为空；
如果队列为空，说明树上不存在两个和为 k 的节点，返回 `False`。

**代码**

```python

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        s = set()
        q = deque([root])
        while q:
            node = q.popleft()
            if k - node.val in s:
                return True
            s.add(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return False        
```

---

### 方法三：深度优先搜索 + 中序遍历 + 双指针
**思路和算法**

注意到二叉搜索树的中序遍历是升序排列的，我们可以将该二叉搜索树的中序遍历的结果记录下来，得到一个升序数组。

这样该问题即转化为「[167. 两数之和 II - 输入有序数组](https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted/)」。我们可以使用双指针解决它。

具体地，我们使用两个指针分别指向数组的头尾，当两个指针指向的元素之和小于 `k` 时，让左指针右移；当两个指针指向的元素之和大于 `k` 时，让右指针左移；当两个指针指向的元素之和等于 `k` 时，返回 `True`。

最终，当左指针和右指针重合时，树上不存在两个和为 `k` 的节点，返回 `False`。

**代码**

```python

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        arr = []
        def inorderTraversal(node: Optional[TreeNode]) -> None:
            if node:
                inorderTraversal(node.left)
                arr.append(node.val)
                inorderTraversal(node.right)
        inorderTraversal(root)

        left, right = 0, len(arr) - 1
        while left < right:
            sum = arr[left] + arr[right]
            if sum == k:
                return True
            if sum < k:
                left += 1
            else:
                right -= 1
        return False
```
