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
        min_val = min(min_val,
                      (matrix[i][j] + matrix[k][j] - matrix[i][k]) // 2)
    return min_val


with open('E:rosalind/rosalind_ba7b.txt', 'r') as f:
    num_leaves = int(f.readline().strip())
    node_j = int(f.readline().strip())
    raw = f.readlines()
    raw0 = list(map(lambda x: x.strip().split(' '), raw))
    matrix_distance0 = []
    for row in raw0:
        temp = list(map(lambda x: int(x), row))
        matrix_distance0.append(temp)

print(limb_length(num_leaves, node_j, matrix_distance0))