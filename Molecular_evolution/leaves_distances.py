from collections import defaultdict


def bfs_implementation(graph, start, end):
    """Implementing breath first seacrh for searching the predecessor of each nodes from start to end.
    After that, using shortest path function, find the shortest length between start node and end node
    input parameters are weighted graph in the form of adjacency list, string start and end nodes
    returns integer of length between start and end nodes."""

    num_nodes = len(graph.keys())
    marked = {str(i): False for i in range(num_nodes)}
    queue = [start]
    predecessor = {}
    while queue:
        current_node = queue.pop(0)

        marked[current_node] = True

        for neighbor in graph[current_node]:
            if marked[neighbor[0]] == False:
                queue.append(neighbor[0])
                predecessor[neighbor[0]] = current_node
    return shortest_path(graph, predecessor, start, end)


def shortest_path(graph, predecessor, start, end):
    """Using predecessor record of the given graph for finding the shortest path and its length from start node to end node
    input paramters are graph in the form of adjacency list, predecessor of graph in dictionary, string start and end node
    returns integer of length."""
    path = [end]
    current_node = end
    length = 0

    while current_node != start:
        current_node = predecessor[current_node]
        path.append(current_node)
        for neighbor in graph[current_node]:
            if neighbor[0] in path:
                length += neighbor[1]

    return length


def distance_between_leaves(n, graph):
    """Creating matrix n x n distance between every leave in the graph
    input parameters are number leaves and graph in the form of adjacency list
    return matrix in the form of nested list."""
    matrix_distance = [[0] * n for _ in range(n)]
    for i in range(len(matrix_distance)):
        for j in range(len(matrix_distance[i])):
            matrix_distance[i][j] = bfs_implementation(graph, str(i), str(j))
    return matrix_distance


with open('E:rosalind/rosalind_ba7a.txt', 'r') as f:
    num_leaves = int(f.readline().strip())
    raw = f.readlines()
    raw0 = list(map(lambda x: x.strip(), raw))
    weighted_graph = defaultdict(list)
    for item in raw0:
        temp = item.split('->')
        temp0 = temp[1].split(':')
        if temp[0] not in weighted_graph:
            weighted_graph[temp[0]] = [[temp0[0], int(temp0[1])]]
        else:
            weighted_graph[temp[0]].append([temp0[0], int(temp0[1])])

result0 = distance_between_leaves(num_leaves, weighted_graph)
for distances in result0:
    for d in distances:
        print(d, end=' ')
    print('\n')