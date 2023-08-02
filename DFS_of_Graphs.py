class Solution:
    def dfsOfGraph(self, V, adj):
        def dfs(vertex, visited, result):
            visited[vertex] = True
            result.append(vertex)
            for neighbor in adj[vertex]:
                if not visited[neighbor]:
                    dfs(neighbor, visited, result)
        
        visited = [False] * V
        result = []
        dfs(0, visited, result)
        return result
