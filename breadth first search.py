from collections import deque
class Graph:
    def BFS(self,n,adj_list,starting_node):
        ans=[]
        starting_node=1
        visited=[0]*(n+1)
        queue=deque()
        adj_List=[
            [],
            [2,8],
            [3,4,1],
            [2],
            [2,5],
            [4,6],
            [7,5],
            [8,6],
            [1,9,7],
            [8]

        ]
        queue.append(starting_node)
        visited[starting_node]=1
        while len(queue) !=0:
            e=queue.popleft()
            ans.append(e)
            for i in adj_List[e]:
                if visited[i]== 0:
                   queue.append(i)
                   visited[i]=1
        return ans            

