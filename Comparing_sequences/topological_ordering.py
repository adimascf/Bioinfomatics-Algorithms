from collections import defaultdict
import collections


def count_in(graph_dict):
    """Counts the number of in degree of every node. Input adjacency list in dictionary """
    in_counts = defaultdict(int)
    for key, val in graph_dict.items():
        for v in val:
            in_counts[v] += 1
    right = []
    for val in graph_dict.values():
        for v in val:
            right.append(v)
    for key in graph_dict.keys():
        if key not in right:
            in_counts[key] = 0
    return in_counts


def topsort_khan(graph):
    """Sorting the nodes in order from a given adjacency list"""
    result = []
    indegrees = count_in(graph)
    queue = collections.deque()

    for node, val in indegrees.items():
        if val == 0:
            queue.append(node)

    while len(queue) > 0:

        vertex = queue.popleft()
        result.append(vertex)
        for node in graph[vertex]:
            indegrees[node] -= 1
            if indegrees[node] == 0:
                queue.append(node)
    return result


def main():

    with open('E://rosalind/rosalind_ba5n.txt', 'r') as file:

        graph = defaultdict(list)
        nodes = set()

        raw_graph = file.readlines()
        for g in raw_graph:
            item = g.strip().split('->')
            nfrom = item[0].replace(' ', '')
            graph[nfrom]

        for key, val in graph.items():
            for g in raw_graph:
                item = g.strip().split('->')
                temp = item[1].replace(' ', '')
                indegrees = temp.split(',')
                if key == item[0].replace(' ', ''):
                    graph[key] = indegrees

    print(dict(graph))

    topological_sort = topsort_khan(graph)
    print(', '.join(topological_sort))


if __name__ == '__main__':
    main()
