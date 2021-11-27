from farthest_first_traversal import eucledian_distance
from collections import defaultdict


def closest_to_center(data_point, centers):

    min_distance = float("inf")
    for c in centers:
        temp = eucledian_distance(c, data_point)
        if temp < min_distance:
            min_distance = temp
            result = c
    return result


def cluster_mean(data, m):

    center = [0] * m
    for data_point in data:
        for i in range(m):
            center[i] += data_point[i]
    center = [x / len(data) for x in center]
    return center


def k_means(data, k, m):

    centers = data[:k]

    while True:

        clusters = defaultdict(list)
        for data_point in data:
            center = closest_to_center(data_point, centers)
            clusters[tuple(center)].append(data_point)

        # recompute the centre
        new_centers = [[]] * k
        for i in range(k):
            new_centers[i] = cluster_mean(clusters[tuple(centers[i])], m)

        if new_centers == centers:
            break
        centers = new_centers[:]
    return centers


if __name__ == "__main__":

    with open("E:genomic_data/dataset_10928_3.txt", "r") as f:
        k_test, m_test = f.readline().strip().split(' ')
        data_test = f.readlines()
        data_test = list(map(lambda item: tuple(
            item.strip().split(" ")), data_test))
        data_test = [tuple(map(lambda x: float(x), item))
                     for item in data_test]

    result = k_means(data_test, int(k_test), int(m_test))
    for center in result:
        result = list(map(lambda x: format(x, ".3f"), center))
        print(*result)
