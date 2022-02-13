class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def bfs(i, j):
            grid[i][j] = 0
            Q = deque([[i, j]])
            while Q:
                i, j = Q.popleft()
                for x, y in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                    if 0 <= x < m and 0 <= y < n and grid[x][y]:
                        grid[x][y] = 0
                        Q.append([x, y])                  

        m, n = len(grid), len(grid[0])
        for i in range(m):
            if grid[i][0] == 1:    bfs(i, 0)
            if grid[i][n-1] == 1:  bfs(i, n-1)   
        for j in range(n):
            if grid[0][j] == 1:    bfs(0, j)
            if grid[m-1][j] == 1:  bfs(m-1, j)
                
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]: ans += 1
        return ans

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
