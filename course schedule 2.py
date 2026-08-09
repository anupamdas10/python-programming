from collections import deque


class Solution:
    def canFinish(self,numCourses,prerequisites ):
        adj_list=[[] for _ in range(numCourses)]
        indegrees=[0]*numCourses
        for u, v in prerequisites :
            adj_list[v].append(u)
            indegrees[u]+=1

        queue=deque()
        result=[]   

        for i in range(0,numCourses):
            if indegrees[i]==0:
                queue.append(i)

        while len(queue)!=0:
            current_node=queue.popleft()
            result.append(current_node)     
            for adjnode in adj_list[current_node] :
                indegrees[adjnode]-=1
                if indegrees[adjnode]==0:
                    queue.append(adjnode)
       
        if len(result)==numCourses:
            return result
        else:
            return []

y=Solution()
r=y.canFinish(4,[[1,0],[2,0],[3,1],[3,2]])        
print(r)