# zip函数

`zip()` 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个`tuple`，然后返回由这些`tuple`组成的对象，这样做的好处是节约了不少的内存。
我们可以使用 `list()` 转换来输出列表。
如果各个迭代器的元素个数不一致，则返回列表长度与最短的对象相同。此外，利用 `*` 号操作符，可以将`tuple`解压为列表。

## 1.并行遍历列表(list)

Python的 `zip()` 函数允许你并行迭代两个或多个可迭代对象。由于 `zip()` 生成`tuple`，可以在 `for循环`的`header`中取出它们：

```python
>>> letters = ['a', 'b', 'c']
>>> numbers = [0, 1, 2]
>>> for l, n in zip(letters, numbers):
...     print(f'Letter: {l}')
...     print(f'Number: {n}')

Letter: a
Number: 0
Letter: b
Number: 1
Letter: c
Number: 2
```
此时,遍历 `zip()` 返回一系列`tuple`并将元素解压缩为 `l` 和 `n`。当结合 `zip()`、`for循环`和`tuple解包`时，就达成了 Python 风格的 Combo! 可用于一次遍历两个或多个可迭代对象。

你还可以在一个 `for循环`中遍历两个以上的可迭代对象。比如示例，它具有三个输入迭代：
```python
>>> letters = ['a', 'b', 'c']
>>> numbers = [0, 1, 2]
>>> operators = ['*', '/', '+']
>>> for l, n, o in zip(letters, numbers, operators):
...     print(f'Letter: {l}')
...     print(f'Number: {n}')
...     print(f'Operator: {o}')
...

Letter: a
Number: 0
Operator: *
Letter: b
Number: 1
Operator: /
Letter: c
Number: 2
Operator: +


```



## 2.并行遍历字典(dictionary)
在 `Python 3.6` 及更高版本中，`dict`是有序集合，这意味着它们将元素保持在与引入时相同的顺序。因此可以使用 `zip()` 以安全连贯的方式遍历多个`dict`：

```python
>>> dict_one = {'name': 'John', 'last_name': 'Doe', 'job': 'Python Consultant'}
>>> dict_two = {'name': 'Jane', 'last_name': 'Doe', 'job': 'Community Manager'}
>>> for (k1, v1), (k2, v2) in zip(dict_one.items(), dict_two.items()):
...     print(k1, '->', v1)
...     print(k2, '->', v2)
...

name -> John
name -> Jane
last_name -> Doe
last_name -> Doe
job -> Python Consultant
job -> Community Manager
```
这里并行遍历了 `dict_one` 和 `dict_two`。此时`zip()` 使用两个`dict`中的`item`生成`tuple`,使用`for循环`取出每个`tuple`并同时访问两个`dict`项目。


## 3.list中行列转换
Python中，`zip(*info)` 即 `zip(*[[1, 2, 3, 4], [5, 6, 7, 8]])` 相当于 `zip([1, 2, 3, 4], [5, 6, 7, 8])`

即 `*[[1, 2, 3, 4], [5, 6, 7, 8]]` 相当于 `[1, 2, 3, 4], [5, 6, 7, 8]`

因此行列互换操作可通过:

```python
>>> matrix = [[3,7,8],[9,11,13],[15,16,17]]
>>> print( list(zip(*matrix)) )

[(3, 9, 15), (7, 11, 16), (8, 13, 17)]

```


---


# Python中多层List展平为一层
```python

import functools
import itertools
import numpy
import operator
import perfplot
from collections import Iterable  # or from collections.abc import Iterable
from iteration_utilities import deepflatten

#使用两次for循环
def forfor(a):
    return [item for sublist in a for item in sublist]

#通过sum
def sum_brackets(a):
    return sum(a, [])

#使用functools內建模块
def functools_reduce(a):
    return functools.reduce(operator.concat, a)

#使用itertools內建模块
def itertools_chain(a):
    return list(itertools.chain.from_iterable(a))

#使用numpy
def numpy_flat(a):
    return list(numpy.array(a).flat)

#使用numpy
def numpy_concatenate(a):
    return list(numpy.concatenate(a))

#自定义函数
def flatten(items):
    """Yield items from any nested iterable; see REF."""
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
            yield from flatten(x)
        else:
            yield x

def pylangs_flatten(a):
    return list(flatten(a))

#使用库iteration_utilities
def iteration_utilities_deepflatten(a):
    return list(deepflatten(a, depth=1))

```
