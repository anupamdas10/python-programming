
from collections import deque


class Solution:
    def incycle(self,V,edges):
        adj_list=[[] for _ in range(V)]
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        visited=[0]*V
        for i in range(0,V):
            if visited[i]==1:
                continue
            queue=deque()
            queue.append((i,-1))
            visited[i]=1
            while len(queue)!=0:
                node,parent=queue.popleft()
                for adjnode in adj_list[node]:
                    if visited[adjnode]==0:
                        queue.append((adjnode,node))
                        visited[adjnode]=1
                    elif parent!=adjnode:
                        return True
            return False

y=Solution()
r=y.incycle(4,[[0, 1], [1, 2], [2, 3]])        
print(r)

