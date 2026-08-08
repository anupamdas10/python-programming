class Solution:
    def dfs(self,current_node,visited,adj_list,stack):
        visited[current_node]=1
        for adjnode in adj_list[current_node]:
            if visited[adjnode]==0:
                self.dfs(adjnode,visited,adj_list,stack)
        stack.append(current_node)

        
    def topoSort(self,V,edges):
        adj_list=[[] for _ in range(V)]
        for u,v in edges:
            adj_list[u].append(v)

        stack=[]
        visited=[0]*V
        for i in range(0,V):
            if visited[i]==0:
                self.dfs(i,visited,adj_list,stack)
        return stack[::-1]            
y=Solution()
r=y.topoSort(6, [[1, 3], [2, 3], [4, 1], [4, 0], [5, 0], [5, 2]])   
print(r)             
