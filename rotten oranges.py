from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
       rows= len(grid) 
       cols= len(grid[0])
       queue= deque()
       
       frsh_cnt=0
       for r in range(rows):
           for c in range(cols):
               if grid[r][c]==2:
                   queue.append((r,c))
               elif grid[r][c]==1:
                      frsh_cnt +=1

       minutes=0
       while len(queue)!=0 and frsh_cnt>0:
           minutes=minutes+1
           total_rotten=len(queue)
           for _ in range(total_rotten):
               i,j = queue.popleft()
               for dx,dy in[(1,0),(-1,0),(0,1),(0,-1)]:
                   new_i,new_j=i+dx,j+dy
                   if new_i<0 or new_i==rows or new_j<0 or new_j==cols:
                       continue
                   if grid[new_i][new_j]==0 or grid[new_i][new_j]==2:
                       continue
                   frsh_cnt-=1
                   grid[new_i][new_j]=2
                   queue.append((new_i,new_j))
       if frsh_cnt >0:
           return -1
       return minutes           

                     
y=Solution()
r=y.orangesRotting([[2,1,1],[1,1,0],[0,1,1]])
print(r)