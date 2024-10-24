# Komşuluk matrisi
adjacency_matrix = [
    [0, 1, 1, 0, 0, 1, 0],
    [1, 0, 0, 1, 1, 0, 0],
    [0, 1, 1, 1, 0, 1, 0],
    [0, 1, 0, 0, 1, 0, 0],
    [1, 0, 1, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 0]
]

def bfs(matrix, start_node):
    visited = [False] * len(matrix)
    queue = [start_node]
    visited[start_node] = True
    bfs_result = []

    while queue:
        node = queue.pop(0)
        bfs_result.append(node)

        for i, connected in enumerate(matrix[node]):
            if connected == 1 and not visited[i]:
                queue.append(i)
                visited[i] = True
    
    return bfs_result

def dfs(matrix, start_node, visited=None, dfs_result=None):
    if visited is None:
        visited = [False] * len(matrix)
    if dfs_result is None:
        dfs_result = []

    visited[start_node] = True
    dfs_result.append(start_node)

    for i, connected in enumerate(matrix[start_node]):
        if connected == 1 and not visited[i]:
            dfs(matrix, i, visited, dfs_result)
    
    return dfs_result

# Örnek kullanım
print("BFS ile dolaşım:", bfs(adjacency_matrix, 0))
print("DFS ile dolaşım:", dfs(adjacency_matrix, 0))