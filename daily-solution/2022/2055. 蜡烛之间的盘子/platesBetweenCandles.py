class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        # 预处理部分
        # 构造前缀和数组
        n = len(s)
        candl = [0]*n
        candr = [-1]*n
        platecnt = [0]*n
        result_list=[]
        for i in range(1, n):
            # 输入参数right从0至n-1开始遍历时，所在位置左侧最近的蜡烛'|'的下标(包括本身)，没有则为0
            candl[i] = i if s[i]=='|' else candl[i-1]
            # 输入参数left从n-1至0开始遍历时，所在位置右侧最近的蜡烛'|'的下标(包括本身)，没有则为-1
            candr[n-i-1] = n-i-1 if s[n-i-1]=='|' else candr[n-i]
            # 所在位置左侧所有盘子个数
            platecnt[i] = platecnt[i-1] + 1 if s[i-1]=='*' else platecnt[i-1]

        for edge in queries:
            result = platecnt[candl[edge[1]]] - platecnt[candr[edge[0]]]
            result_list.append(result if result>=0 else 0)
            # print(f'left[{edge[0]}]: {candr[edge[0]]}\nright[{edge[1]}]: {candl[edge[1]]}\nplate num: {platecnt[candl[edge[1]]] - platecnt[candr[edge[0]]]}\n\n')

        # print(f'{s}\n\nRight: {candl}\nLeft: {candr}\nPlate number: {platecnt}')
        return result_list
