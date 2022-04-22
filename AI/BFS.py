visited = []  # List for visited nodes.
queue = []  # Initialize a queue


def bfs(visited, graph, node):  # function for BFS
  visited.append(node)
  queue.append(node)

  while queue:          # Creating loop to visit each node
    m = queue.pop(0)
    print(m, end=" ")

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)


# eg 1
# graph = {
#     '0': ['1', '2'],
#     '1': ['2'],
#     '2': ['0', '3'],
#     '3': ['3'],
# }

# print("Following is the Breadth-First Search")
# bfs(visited, graph, '2')    # function calling
# op 1
# 2 0 3 1

# eg 2
graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}
print("Following is the Breadth-First Search")
bfs(visited, graph, '5')
# op 2
# 5 3 7 2 4 8