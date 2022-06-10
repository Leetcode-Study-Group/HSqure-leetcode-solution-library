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
            for node in root.children:
                predfs(node)
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
            for node in root.children:
                posdfs(node)
            res.append(root.val)
        posdfs(root)
        return res
```

---

# Part 4. 层序遍历
逐层地从左到右访问所有节点。

## 102. 二叉树的层序遍历
给你二叉树的根节点 `root` ，返回其节点值的 **层序遍历** 。 
示例:

```python
输入：root = [3,9,20,null,null,15,7]

       3
     /   \
    9     20     
          / \   
         15  7

输出：[[3],[9,20],[15,7]]
```
### 题解

```python
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res=[]
        # Breadth-First Search
        def bfs(root: TreeNode, deepth):
            if not root:
                return
            # 为每一层新建一个维度的list
            if len(res)-1 < deepth:
                res.append([])
            bfs(root.left, deepth+1)
            res[deepth].append(root.val)
            bfs(root.right, deepth+1)
        bfs(root,0)
        return res

```

## 429. N 叉树的层序遍历
给定一个 **N 叉树**，返回其节点值的**层序遍历**。（即从左到右，逐层遍历）。

树的序列化输入是用层序遍历，每组子节点都由 `null` 值分隔（参见示例）。

示例：

```python

输入：root = [1,null,3,2,4,null,5,6]

        1
     /  |  \
    3   2   4
   / \   
  5   6

输出：[[1],[3,2,4],[5,6]]

```

### 题解

```python

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res=[]
        def bfs(root: 'Node', deepth):
            if not root:
                return
            if len(res)-1 < deepth:
                res.append([])
            # 先序或者后序dfs都可,然后根据deepth来收集每层的元素来达成bfs
            res[deepth].append(root.val)
            for node in root.children:
                bfs(node, deepth+1)
        bfs(root, 0)
        return res

```
### 题解2

```python

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return
        res=[]
        # 创建队列
        q = deque([root])
        while q:
            level=[]
            for _ in range(len(q)):
                cur = q.popleft()
                level.append(cur.val)
                for child in cur.children:
                    q.append(child)
            res.append(level)
         return res


```

# Part 5. 综合

## 617. 合并二叉树
给你两棵二叉树： `root1` 和 `root2` 。

想象一下，当你将其中一棵覆盖到另一棵之上时，两棵树上的一些节点将会重叠（而另一些不会）。你需要将这两棵树合并成一棵新二叉树。合并的规则是：如果两个节点重叠，那么将这两个节点的值相加作为合并后节点的新值；否则，不为 `null` 的节点将直接作为新二叉树的节点。

返回合并后的二叉树。

注意: 合并过程必须从两个树的根节点开始。
 

示例1：
```python

```python
输入：root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
输出：[3,4,5,5,4,null,7]
```

示例 2：
```python
输入：root1 = [1], root2 = [1,2]
输出：[2,2]
```

### 题解

```python




```
