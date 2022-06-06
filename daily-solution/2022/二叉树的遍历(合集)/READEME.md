# Part 1. 前序遍历
PreOrder, 按照先访问根节点的顺序。

## 144. 二叉树的前序遍历
给你二叉树的根节点 `root` ，返回它节点值的 **前序** 遍历。

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


### 题解1:

```python

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        # Pre-Order Deep-First Search
        def pdfs(root: TreeNode):
            if not root:
                return
            res.append(root.val)
            pdfs(root.left)
            pdfs(root.right)
        pdfs(root)
        return res
```
## 589. N叉树的前序遍历
给定一个 **n 叉树**的根节点 `root` ，返回 其节点值的 **前序遍历** 。

**n 叉树** 在输入中按层序遍历进行序列化表示，每组子节点由空值 `null` 分隔（请参见示例）。

示例 1：
```python
输入：root = [1,null,3,2,4,null,5,6]

        1
     /  |  \
    3   2   4
   / \   
  5   6

输出：[1,3,5,6,2,4]
```
### 题解

```python
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        # Pre-Order Deep-First Search
        def pdfs(node: 'Node'):
            if node is None:
                return
            ans.append(node.val)
            for ch in node.children:
                pdfs(ch)
        pdfs(root)
        return res
```

---

# Part 2. 中序遍历
InOrder, 按照根节点在中间访问的顺序

## 94. 二叉树的中序遍历
给定一个二叉树的根节点 `root` ，返回 它的 **中序** 遍历 。

示例 1：
```python
输入：root = [1,null,2,3]

       1
         \
          2
         /    
        3  

输出：[1,3,2]
```
### 题解

```python
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans = []
        # In-Order Deep-First Search
        def idfs(root: TreeNode):
            if not root:
                return
            idfs(root.left)
            res.append(root.val)
            idfs(root.right)
        idfs(root)
        return res
```
