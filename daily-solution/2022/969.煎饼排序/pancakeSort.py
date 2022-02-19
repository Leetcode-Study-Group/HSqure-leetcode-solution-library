class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        # 翻转操作，返回操作后的数组和翻转记录
        def upsidedown(num_list, pos, k_list):
            k_list.append(pos)
            tmp = num_list[:pos]
            tmp.reverse()
            return tmp + num_list[pos:], k_list

        k_list = []
        max_num = len(arr)

        while max_num!=1:
            # 如果当前范围最大数已经在正确的位置，则跳过此轮排序
            if arr[max_num-1] == max_num:
                max_num-=1
                continue
            # 第一步：取当前范围最大的数作为最后一个的所在list翻转至第一个
            arr, k_list = upsidedown(arr, arr.index(max_num)+1, k_list)
            # 第二步：将当前范围整体翻转，此时最大的数字就回到正确位置了
            arr, k_list = upsidedown(arr, max_num, k_list)
            # 将最后一个排好的数排除在外（不会被影响），缩小范围，重复
            max_num-=1
        return k_list
