with open('sars_non_additive.txt', 'r') as f:
    num_leaves = int(f.readline().strip())
    raw = f.readlines()
    raw0 = list(map(lambda x: x.strip().split('\t'), raw))
    matrix_distance_test = []
    for row in raw0:
        temp = list(map(lambda x: int(x), row))
        matrix_distance_test.append(temp)


def upgma_pyhlo(matrix, n_leaves):
    """Creating phylogeny tree based on UPGMA (Unweighted Pair Group Method with Arithmetic Mean) algorithm
    input parameters are matrix distance in the form of a nested list and integer of number of present day species (leaves)
    returns a nested list [node, node, weight]"""

    edges = []

    matrix_dict = {}
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i not in matrix_dict:
                matrix_dict[i] = {j: matrix[i][j]}
            else:
                matrix_dict[i][j] = matrix[i][j]

    clusters = {i: [i] for i in range(n_leaves)}

    new_node_label = n_leaves
    graph_T = []
    age_leaves = {i: 0 for i in range(n_leaves)}
    age = 0

    while len(matrix_dict) > 1:

        node_i, node_j = 0, 0
        min_distance = float('inf')
        nodes = list(matrix_dict.keys())

        for i in range(len(nodes)-1):
            for j in range(i+1, len(nodes)):
                if min_distance > matrix_dict[nodes[i]][nodes[j]]:
                    min_distance = matrix_dict[nodes[i]][nodes[j]]
                    node_i, node_j = nodes[i], nodes[j]

        new_cluster = clusters[node_i] + clusters[node_j]

        graph_T = [[new_node_label, node_i], [new_node_label, node_j]]

        age = matrix_dict[node_i][node_j]/2

        matrix_dict[new_node_label] = {}
        matrix_dict[new_node_label][new_node_label] = 0

        for old_node in nodes:
            total = 0
            count = 0
            for init_node in clusters[old_node]:
                for node in new_cluster:
                    total += matrix[init_node][node]
                    count += 1

            # Adds new key in matrix dictionary from combining row and column of matrix list
            matrix_dict[old_node][new_node_label] = total/count
            matrix_dict[new_node_label][old_node] = total/count

        clusters[new_node_label] = new_cluster
        age_leaves[new_node_label] = age
        new_node_label += 1

        # Deletes row and column in i and j
        del matrix_dict[node_i]
        del matrix_dict[node_j]

        for key in matrix_dict.keys():
            del matrix_dict[key][node_i]

        for key in matrix_dict.keys():
            del matrix_dict[key][node_j]

        # Append the edge and the weigh to the edges variable
        for edge in graph_T:
            length = age - age_leaves[edge[1]]
            edges.append(edge + [length])
            edges.append(edge[::-1] + [length])

    edges.sort(key=lambda x: x[1])
    edges.sort(key=lambda x: x[0])

    return edges


result = (upgma_pyhlo(matrix_distance_test, num_leaves))
conversion = {0: 'Cow', 1: 'Pig', 2: 'Horse', 3: 'Mouse',
              4: 'Dog', 5: 'Cat', 6: 'Turkey', 7: 'Civet', 8: 'Human'}

for item in result:
    node1, node2, weight = item
    if node1 in conversion:
        node1 = conversion[node1]
    else:
        node1 = node1
    if node2 in conversion:
        node2 = conversion[node2]
    else:
        node2 = node2
    print(f"{str(node1)}->{str(node2)}:{format(weight, '.3f')}")
