from collections import deque
class Solution:
    def toposort(self,V,edges):
         adj_list=[[] for _ in range(V)]
         indegrees=[0]*V
         for u, v in edges:
              adj_list[u].append(v)
              indegrees[v]+=1
         queue=deque()
         result=[]
         for i in range(0,V):
              if indegrees[i]==0:
                   queue.append(i)
         while len(queue)!=0:
              current_node=queue.popleft()
              result.append(current_node)
              for adjnode in adj_list[current_node]:
                   indegrees[adjnode]-=1
                   if indegrees [adjnode]==0:
                        queue.append(adjnode)
         return result
y=Solution()
r = y.toposort(4, [[3, 0], [1, 0], [2, 0]])
print(r)

                       


