from math import sqrt


def eucledian_distance(point_a, point_b):
    """Calculating distance between two points in m dimensional
    input parameters are two coordinates in tuple
    returns integer"""
    result = 0
    for i in range(len(point_a)):
        dist = (point_a[i] - point_b[i])**2
        result += dist
    result = sqrt(result)
    return result


def distance_from_centers(centers, point):
    """Calculating distance from every center to a given point.
    input paramters are coordinates in tuple
    returns integer"""
    result = float("inf")
    for c in centers:
        dist = eucledian_distance(c, point)
        if dist < result:
            result = dist
    return result


def max_distance(data, center):
    """Calculating the maximum distance for each center and data.
    input parameters are lists of tuple coordinates
    returns a coordinat that has a max distance from center"""
    max_dist = -float("inf")
    for d in data:
        temp = distance_from_centers(center, d)
        if temp > max_dist:
            max_dist = temp
            result = d
    return result


def farthest_first_traversal(data, k):
    """Finding k coodinates as center"""
    centers = [data[0]]
    while len(centers) < k:
        data_point = max_distance(data, centers)
        centers.append(data_point)
    return centers


if __name__ == "__main__":

    with open("E:genomic_data/dataset_38039_2.txt", "r") as f:
        k_test, m_test = f.readline().strip().split(' ')
        data_test = f.readlines()
        data_test = list(map(lambda item: tuple(
            item.strip().split(" ")), data_test))
        data_test = [tuple(map(lambda x: float(x), item))
                     for item in data_test]

    for i in farthest_first_traversal(data_test, int(k_test)):
        print(*i)
