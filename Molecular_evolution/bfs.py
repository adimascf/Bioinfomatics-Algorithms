def bfs_shortespath(graph, start, end):
    visited_nodes = []
    queue = [start]
    predecessor = {}

    while queue:
        curr_node = queue.pop(0)
        visited_nodes.append(curr_node)
        for neighbor in graph[curr_node]:
            if neighbor not in visited_nodes:
                queue.append(neighbor)
                predecessor[neighbor] = curr_node

    return shortestpath(predecessor, start, end)


def shortestpath(predecessor_node, start, end):

    path = [end]
    curr_node = end
    while curr_node != start:
        curr_node = predecessor_node[curr_node]
        path.append(curr_node)
    path.reverse()
    return path


test_graph = {'0': ['3', '5', '9'],
              '1': ['6', '7', '4'],
              '2': ['10', '5'],
              '3': ['0'],
              '4': ['1', '5', '8'],
              '5': ['2', '0', '4'],
              '6': ['1'],
              '7': ['1'],
              '8': ['4'],
              '9': ['0'],
              '10': ['2']
              }

print(*bfs_shortespath(test_graph, '0', '10'), sep=' -> ')
