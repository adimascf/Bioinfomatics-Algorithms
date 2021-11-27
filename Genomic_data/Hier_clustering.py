with open('E:genomic_data/dataset_10934_7.txt', 'r') as f:
    n_test = int(f.readline().strip())
    raw = f.readlines()
    raw0 = list(map(lambda x: x.strip().split(' '), raw))
    matrix_distance_test = []
    for row in raw0:
        temp = list(map(lambda x: float(x), row))
        matrix_distance_test.append(temp)


def hierarchical_clustering(n_genes, matrix_distance, D="avg"):
    """Input: An integer n, followed by an n x n distance matrix.
    Output: The result of applying HierarchicalClustering to this distance matrix (using Davg, Dmin, or Dmax), 
    with each newly created cluster listed on each line."""

    clusters = [[i] for i in range(n_genes)]

    new_clusters_list = []

    while len(clusters) > 1:

        lenght = len(clusters)
        min_distance = float("inf")
        for i in range(lenght-1):
            for j in range(i+1, lenght):
                if D == "min":
                    distance = -float("inf")
                    for idx1 in clusters[i]:
                        for idx2 in clusters[j]:
                            current = matrix_distance[idx1][idx2]
                            if current < distance:
                                distance = current
                elif D == "avg":
                    distance = 0
                    for idx1 in clusters[i]:
                        for idx2 in clusters[j]:
                            current = matrix_distance[idx1][idx2]
                            distance += current
                    distance = distance / (len(clusters[i]) * len(clusters[j]))
                elif D == "max":
                    distance = float("inf")
                    for idx1 in clusters[i]:
                        for idx2 in clusters[j]:
                            current = matrix_distance[idx1][idx2]
                            if current > distance:
                                distance = current

                if distance < min_distance:
                    min_distance = distance
                    closest1 = i
                    closest2 = j

        # Merge the two closest to one cluster
        new_clusters = clusters[closest1] + clusters[closest2]
        clusters = [c for c in clusters if c not in [
            clusters[closest1], clusters[closest2]]]
        clusters.append(new_clusters)
        new_clusters_list.append(new_clusters)

    return new_clusters_list


for c in hierarchical_clustering(n_test, matrix_distance_test):
    temp = list(map(lambda x: x+1, c))
    print(*temp)
