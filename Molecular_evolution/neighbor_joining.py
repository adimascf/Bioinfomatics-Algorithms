def neighbor_joining_matrix(matrix_distance_dict):
    """Creating neighbor joining matrix distance from original matrix distance
    input paramter is matrix distance in dictionary, returns dictionary"""

    result = {}
    for key1, val1 in matrix_distance_dict.items():
        for key2, val2 in matrix_distance_dict[key1].items():
            if key1 not in result:
                result[key1] = {}
            if key1 == key2:
                result[key1][key2] = 0
            else:
                result[key1][key2] = (len(matrix_distance_dict) - 2) * val2 - sum(
                    matrix_distance_dict[key1].values()) - sum(matrix_distance_dict[key2].values())
    return result


def neighbor_joining_pyhlo(matrix_distance_dict):
    """Constructing phylogeny tree using neighbor joining algorithm
    input paramter is dictionary matrix distance, 
    returns graph in a nested list """

    n = len(matrix_distance_dict)
    if n == 2:  # base case, kalo n sudah tinggal 2 maka recursive berhenti dan akan mengeluarkan output
        # initializes output from the base case
        idx = list(matrix_distance_dict.keys())
        tree_graph = [[idx[0], idx[1], matrix_distance_dict[idx[0]][idx[1]]], [
            idx[1], idx[0], matrix_distance_dict[idx[0]][idx[1]]]]
        return tree_graph

    nj_matrix = neighbor_joining_matrix(matrix_distance_dict)

    # Finds the minimum distance in nj matrix
    min_distance = float('inf')
    idx1, idx2 = 0, 0
    for key1, val1 in nj_matrix.items():
        for key2, val2 in nj_matrix[key1].items():
            if key1 != key2 and val2 < min_distance:
                min_distance = val2
                idx1, idx2 = key1, key2

    # calculates the limb length from parent node to both nodes(leaves)
    delta = (sum(matrix_distance_dict[idx1].values(
    )) - sum(matrix_distance_dict[idx2].values())) / (n - 2)
    limb_length1 = (matrix_distance_dict[idx1][idx2] + delta) / 2
    limb_length2 = (matrix_distance_dict[idx1][idx2] - delta) / 2

    # creates new cluster
    m = max(list(matrix_distance_dict.keys())) + 1

    for key in matrix_distance_dict.keys():
        matrix_distance_dict[key][m] = (
            matrix_distance_dict[idx1][key] + matrix_distance_dict[key][idx2] - matrix_distance_dict[idx1][idx2]) / 2

    matrix_distance_dict[m] = {}
    for key in matrix_distance_dict.keys():
        matrix_distance_dict[m][key] = (
            matrix_distance_dict[idx1][key] + matrix_distance_dict[key][idx2] - matrix_distance_dict[idx1][idx2]) / 2

    matrix_distance_dict[m][m] = 0

    # deletes nodes that have been combine to cluster
    del matrix_distance_dict[idx1]
    del matrix_distance_dict[idx2]

    for key in matrix_distance_dict.keys():
        del matrix_distance_dict[key][idx1]
        del matrix_distance_dict[key][idx2]

    tree_graph = neighbor_joining_pyhlo(matrix_distance_dict)

    # adding two new limbs connecting two nodes
    tree_graph.append([idx1, m, limb_length1])
    tree_graph.append([m, idx1, limb_length1])
    tree_graph.append([idx2, m, limb_length2])
    tree_graph.append([m, idx2, limb_length2])

    return tree_graph


with open('E:molecular_evolution/sars_non_additive.txt', 'r') as f:
    num_leaves = int(f.readline().strip())
    raw = f.readlines()
    raw0 = list(map(lambda x: x.strip().split('\t'), raw))
    matrix_distance_test = []
    for row in raw0:
        temp = list(map(lambda x: int(x), row))
        matrix_distance_test.append(temp)

    matrix_dict = {}
    for i in range(len(matrix_distance_test)):
        for j in range(len(matrix_distance_test[0])):
            if i not in matrix_dict:
                matrix_dict[i] = {j: matrix_distance_test[i][j]}
            else:
                matrix_dict[i][j] = matrix_distance_test[i][j]

result = neighbor_joining_pyhlo(matrix_dict)
result.sort(key=lambda x: x[0])
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
