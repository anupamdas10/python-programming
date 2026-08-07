class Solution:

    def dfs(self, current_node, visited, path_visited, adj_list):

        visited[current_node] = 1
        path_visited[current_node] = 1

        for adjnode in adj_list[current_node]:

            if visited[adjnode] == 0:

                x = self.dfs(
                    adjnode,
                    visited,
                    path_visited,
                    adj_list
                )

                if x == True:
                    return True

            elif path_visited[adjnode] == 1:
                return True

        path_visited[current_node] = 0
        return False

    def isCyclic(self, V, edges):

        adj_list = [[] for _ in range(V)]

        for u, v in edges:
            adj_list[u].append(v)

        visited = [0] * V
        path_visited = [0] * V

        for i in range(V):

            if visited[i] == 0:

                ans = self.dfs(
                    i,
                    visited,
                    path_visited,
                    adj_list
                )

                if ans == True:
                    return True

        return False


y = Solution()

r = y.isCyclic(
    4,
    [[0, 1], [1, 2], [2, 0], [2, 3]]
)

print(r)
y = Solution()
r = y.isCyclic(4, [[0,1], [1,2], [2,0], [2,3]])
print(r)