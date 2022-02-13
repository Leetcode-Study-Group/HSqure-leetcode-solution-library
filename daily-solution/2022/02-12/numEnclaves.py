# class Solution:
#     def connetSearch(self,matrix1,matrix2):
#         r_addr=[]
#         c_addr=[]
#         for i in range(0,len(matrix1)):
#             if not i==0:
#                 if matrix2[i]&matrix2[i-1]:

#                     # 显示在第r行中，与本行前一个(i-1)有连通的位置i
#                     # r_addr.append(i)
#             if matrix1[i]&matrix2[i]:
#                 # 显示在第r行中，与上一行(r-1)有联通的位置i
#                 c_addr.append(i)
#         return r_addr, c_addr

#     def numEnclaves(self, grid: List[List[int]]) -> int:
#         for r in range(1,len(grid)):
#             print(f'row{r-1} to row{r}:')
#             r_search, c_search = self.connetSearch(grid[r-1],grid[r])
            

#             print(f'row search:\n{r_search}\ncolumn search:\n{c_search}\n\n')
