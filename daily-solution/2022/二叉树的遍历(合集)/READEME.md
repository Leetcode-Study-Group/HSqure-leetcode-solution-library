# 144. 二叉树的前序遍历

给你二叉树的根节点 root ，返回它节点值的 前序 遍历。

示例 1:
```python
输入: root = [1,null,2,3]
       1
         \
          2
         /    
        3     

输出: [1,2,3]

```

示例 2：
```python
输入：root = [1]
输出：[1]
```

示例 3:
```python
输入: root = [1,2]
       1
      /  
     2

输出: [1,2]

```
## 题解1:

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def traversal(root: TreeNode):
            if not root:
                return
            res.append(root.val)
            traversal(root.left)
            traversal(root.right)
        traversal(root)
        return res
```
