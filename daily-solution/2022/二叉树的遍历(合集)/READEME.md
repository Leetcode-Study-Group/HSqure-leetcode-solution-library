# Part 1. 前序遍历
PreOrder, 按照先访问根节点的顺序。

## 144. 二叉树的前序遍历
给你二叉树的根节点 `root` ，返回它节点值的 **前序** 遍历。

示例:
```python
输入: root = [1,null,2,3]

       1
         \
          2
         /    
        3     

输出: [1,2,3]

```


### 题解:

```python

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        # Pre-Order Deep-First Search
        def predfs(root: TreeNode):
            if not root:
                return
            res.append(root.val)
            predfs(root.left)
            predfs(root.right)
        predfs(root)
        return res
```
## 589. N叉树的前序遍历
给定一个 **n 叉树**的根节点 `root` ，返回 其节点值的 **前序遍历** 。
predfs
**n 叉树** 在输入中按层序遍历进行序列化表示，每组子节点由空值 `null` 分隔（请参见示例）。

示例：
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
        def predfs(root: 'Node'):
            if not root:
                return
            res.append(root.val)
            for ch in root.children:
                predfs(ch)
        predfs(root)
        return res
```

---

# Part 2. 中序遍历
InOrder，按照根节点在中间访问的顺序，**N叉树**无**中序**遍历。

## 94. 二叉树的中序遍历
给定一个二叉树的根节点 `root` ，返回它的 **中序** 遍历 。

示例：
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
    def inorderTraversal(self, root: 'Node') -> List[int]:
        res = []
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

---

# Part 3. 后序遍历
PosterOrder, 按照根节点在后面访问的顺序

## 145. 二叉树的后序遍历

示例：
```python
输入：root = [1,null,2,3]

       1
         \
          2
         /    
        3  

输出：[3,2,1]
```

### 题解

```python
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        # Poster-Order Deep-First Search
        def posdfs(root: TreeNode):
            if not root:
                return
            posdfs(root.left)
            posdfs(root.right)
            res.append(root.val)
        posdfs(root)
        return res
```

## 590. N 叉树的后序遍历

示例：
```python
输入：root = [1,null,3,2,4,null,5,6]

        1
     /  |  \
    3   2   4
   / \   
  5   6

输出：[5,6,3,2,4,1]
```

### 题解

```python
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res=[]
        def posdfs(root: 'Node'):
            if not root:
                return
            for ch in root.children:
                posdfs(ch)
            res.append(root.val)
        posdfs(root)
        return res
```

---
