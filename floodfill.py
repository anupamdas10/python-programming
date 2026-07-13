from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
         return image
        rows= len(image) 
        cols= len(image[0])
        initial_color=image[sr][sc]
        queue=deque()
        queue.append((sr,sc))
        while len(queue)!=0:
            i,j=queue.popleft()
            image[i][j]=color
            for dx,dy in[(0,1),(0,-1),(1,0),(-1,0)]:
                new_i=dx+i
                new_j=dy+j
                if new_i<0 or new_i>=rows or new_j<0 or new_j>=cols:
                    continue                   
                if image[new_i][new_j]!=initial_color:
                    continue
                queue.append((new_i,new_j))
        return image        
    
y=Solution()
r=y.floodFill([[1,1,1],[1,1,0],[1,0,1]],1,1, 3)
print(r)                  
