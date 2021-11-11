def limb_length(n, j, matrix):
    """Calculating the limb length of species j.
    input parameters are matrix in a nested list, and an integer j. returns an integer"""
    min_val = float('inf')
    i = 0
    while i < n and i == j:
        i += 1
    for k in range(n):
        if k == j or k == i:
            continue
        min_val = min(min_val, (matrix[i][j] + matrix[k][j] - matrix[i][k])//2)
    return min_val


def find_path(tree, start, end):

    marked = {i: False for i in tree['edges'].keys()}
    pred = {i: None for i in tree['edges'].keys()}

    marked[start] = True
    queue = [start]
    while queue:
        u = queue.pop(0)
        for v in tree['edges'][u]:
            if not marked[v]:
                marked[v] = True
                pred[v] = u
                if v == end:
                    break
                queue.append(v)
    path = []
    u = end
    while u != None:
        path.append(u)
        u = pred[u]
    path.reverse()
    return path


def attach_node(tree, start, end, node, path_length, length_of_limb):

    path = find_path(tree, start, end)

    i = 0
    while i < len(path) - 1:
        weight = tree['edges'][path[i]][path[i+1]]
        if path_length <= weight:
            break
        path_length -= weight
        i += 1

    if path_length < tree['edges'][path[i]][path[i+1]]:
        a = path[i]
        b = path[i+1]
        del tree['edges'][a][b]
        del tree['edges'][b][a]

        v = tree['internal_node_counter']
        tree['edges'][v] = {}

        tree['edges'][a][v] = tree['edges'][v][a] = path_length
        tree['edges'][b][v] = tree['edges'][v][b] = weight - path_length

        tree['edges'][node] = {v: length_of_limb}
        tree['edges'][v][node] = length_of_limb
        tree['internal_node_counter'] += 1
    else:
        b = path[i+1]
        tree['edges'][node] = {b: length_of_limb}
        tree['edges'][b][node] = length_of_limb


def additive_phylogeny(matrix, num_nodes):

    n = len(matrix)
    if n == 2:
        tree = {
            'edges': {
                0: {1: matrix[0][1]},
                1: {0: matrix[1][0]}
            },
            'num_nodes': 2,
            'internal_node_counter': num_nodes
        }
        return tree

    get_limb_length = limb_length(n, n-1, matrix)

    # Compute matrix bald
    for j in range(n-1):
        matrix[j][n-1] -= get_limb_length
        matrix[n-1][j] = matrix[j][n-1]

    i, k = 0, 0
    while matrix[i][k] != matrix[i][n-1] + matrix[n-1][k] or i == k:
        k += 1
    x = matrix[i][n-1]

    trimmed_matrix = [[matrix[i][j] for j in range(n-1)] for i in range(n-1)]
    tree = additive_phylogeny(trimmed_matrix, num_nodes)

    attach_node(tree, i, k, n-1, x, get_limb_length)

    # restore lengths
    for j in range(n-1):
        matrix[j][n-1] += get_limb_length
        matrix[n-1][j] = matrix[j][n-1]

    return tree


def print_tree(tree):

    for u in sorted(tree['edges']):
        for v in sorted(tree['edges'][u]):
            print(f"{u}->{v}:{tree['edges'][u][v]}")


with open('E:molecular_evolution/additive_phy.txt', 'r') as f:
    num_leaves = int(f.readline().strip())
    raw = f.readlines()
    raw0 = list(map(lambda x: x.strip().split('\t'), raw))
    matrix_distance_test2 = []
    for row in raw0:
        temp = list(map(lambda x: int(x), row))
        matrix_distance_test2.append(temp)

result = additive_phylogeny(matrix_distance_test2, num_leaves)
print_tree(result)
