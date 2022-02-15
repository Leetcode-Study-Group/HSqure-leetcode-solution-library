# 540. 有序数组中的单一元素
给你一个仅由整数组成的有序数组，其中每个元素都会出现两次，唯有一个数只会出现一次。
请你找出并返回只出现一次的那个数。
你设计的解决方案必须满足 `O(log n)` 时间复杂度和 `O(1)` 空间复杂度。

 

**示例 1:**

输入: nums = [1,1,2,3,3,4,4,8,8]
输出: 2

**示例 2:**

输入: nums =  [3,3,7,7,10,11,11]
输出: 10
 

提示:

- `1 <= nums.length <= 105`
- `0 <= nums[i] <= 105`

## 题解

### 最优题解

#### 方法一：全数组的二分查找
**思路和算法**

假设只出现一次的元素位于下标 xx，由于其余每个元素都出现两次，因此下标 xx 的左边和右边都有偶数个元素，数组的长度是奇数。

由于数组是有序的，因此数组中相同的元素一定相邻。对于下标 xx 左边的下标 yy，如果 \textit{nums}[y] = \textit{nums}[y + 1]nums[y]=nums[y+1]，则 yy 一定是偶数；对于下标 xx 右边的下标 zz，如果 \textit{nums}[z] = \textit{nums}[z + 1]nums[z]=nums[z+1]，则 zz 一定是奇数。由于下标 xx 是相同元素的开始下标的奇偶性的分界，因此可以使用二分查找的方法寻找下标 xx。

初始时，二分查找的左边界是 00，右边界是数组的最大下标。每次取左右边界的平均值 \textit{mid}mid 作为待判断的下标，根据 \textit{mid}mid 的奇偶性决定和左边或右边的相邻元素比较：

如果 \textit{mid}mid 是偶数，则比较 \textit{nums}[\textit{mid}]nums[mid] 和 \textit{nums}[\textit{mid} + 1]nums[mid+1] 是否相等；

如果 \textit{mid}mid 是奇数，则比较 \textit{nums}[\textit{mid} - 1]nums[mid−1] 和 \textit{nums}[\textit{mid}]nums[mid] 是否相等。

如果上述比较相邻元素的结果是相等，则 \textit{mid} < xmid<x，调整左边界，否则 \textit{mid} \ge xmid≥x，调整右边界。调整边界之后继续二分查找，直到确定下标 xx 的值。

得到下标 xx 的值之后，\textit{nums}[x]nums[x] 即为只出现一次的元素。

细节

利用按位异或的性质，可以得到 \textit{mid}mid 和相邻的数之间的如下关系，其中 \oplus⊕ 是按位异或运算符：

当 \textit{mid}mid 是偶数时，\textit{mid} + 1 = \textit{mid} \oplus 1mid+1=mid⊕1；

当 \textit{mid}mid 是奇数时，\textit{mid} - 1 = \textit{mid} \oplus 1mid−1=mid⊕1。

因此在二分查找的过程中，不需要判断 \textit{mid}mid 的奇偶性，\textit{mid}mid 和 \textit{mid} \oplus 1mid⊕1 即为每次需要比较元素的两个下标。

**代码**

```python
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] == nums[mid ^ 1]:
                low = mid + 1
            else:
                high = mid
        return nums[low]
```
**复杂度分析**

时间复杂度：O(\log n)O(logn)，其中 nn 是数组 \textit{nums}nums 的长度。需要在全数组范围内二分查找，二分查找的时间复杂度是 O(\log n)O(logn)。

空间复杂度：O(1)O(1)。

#### 方法二：偶数下标的二分查找
**思路和算法**

由于只出现一次的元素所在下标 xx 的左边有偶数个元素，因此下标 xx 一定是偶数，可以在偶数下标范围内二分查找。二分查找的目标是找到满足 \textit{nums}[x] \ne \textit{nums}[x + 1]nums[x] 
	
 =nums[x+1] 的最小的偶数下标 xx，则下标 xx 处的元素是只出现一次的元素。

初始时，二分查找的左边界是 00，右边界是数组的最大偶数下标，由于数组的长度是奇数，因此数组的最大偶数下标等于数组的长度减 11。每次取左右边界的平均值 \textit{mid}mid 作为待判断的下标，如果 \textit{mid}mid 是奇数则将 \textit{mid}mid 减 11，确保 \textit{mid}mid 是偶数，比较 \textit{nums}[\textit{mid}]nums[mid] 和 \textit{nums}[\textit{mid} + 1]nums[mid+1] 是否相等，如果相等则 \textit{mid} < xmid<x，调整左边界，否则 \textit{mid} \ge xmid≥x，调整右边界。调整边界之后继续二分查找，直到确定下标 xx 的值。

得到下标 xx 的值之后，\textit{nums}[x]nums[x] 即为只出现一次的元素。

**细节**

考虑 \textit{mid}mid 和 11 按位与运算的结果，其中 \&& 是按位与运算符：

- 当 \textit{mid}mid 是偶数时，\textit{mid}~\&~1 = 0mid & 1=0；

- 当 \textit{mid}mid 是奇数时，\textit{mid}~\&~1 = 1mid & 1=1。

因此在得到 \textit{mid}mid 的值之后，将 \textit{mid}mid 的值减去 \textit{mid}~\&~1mid & 1，即可确保 \textit{mid}mid 是偶数，如果原来的 \textit{mid}mid 是偶数则值不变，如果原来的 \textit{mid}mid 是奇数则值减 11。

**代码**

```python
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high) // 2
            mid -= mid & 1
            if nums[mid] == nums[mid + 1]:
                low = mid + 2
            else:
                high = mid
        return nums[low]
```

复杂度分析

时间复杂度：O(\log n)O(logn)，其中 nn 是数组 \textit{nums}nums 的长度。需要在偶数下标范围内二分查找，二分查找的时间复杂度是 O(\log n)O(logn)。

空间复杂度：O(1)O(1)。



```python
```

### 我的题解
**思路:**
拿`奇数-1`(因为数组下标0起始)的和下一个进行比对,如果不相同则记录前一个并退出.
此外,**注意边界值**:最后一个没有下一个用来比对了,因为数组数字的数量**必然为奇数**,因此`while`的条件就成了**提前在上一次奇数处停下**,如果此时此前一直都成对,那么最后一个必然是单身狗🐶.这样就可以防止边界值溢出.
```python
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n=0
        i=0
        result = nums[0]
        while n < len(nums) - 2:
            n = 2 * i + 1
            # 比对
            if nums[n-1] != nums[n]:
                result = nums[n-1]
                break
            i+=1
            result = nums[n+1]

        return result

```
`Date 2/14`
