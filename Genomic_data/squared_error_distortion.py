from farthest_first_traversal import distance_from_centers

with open("E:genomic_data/dataset_10927_3.txt", "r") as f:
    k_test, m_test = f.readline().strip().split(' ')
    raw = f.read().strip().split('--------')
    centers_test = raw[0].strip().split('\n')
    data_test = raw[1].strip().split('\n')
    centers_test = list(map(lambda x: tuple(x.split(' ')), centers_test))
    centers_test = [tuple(map(lambda x: float(x), item))
                    for item in centers_test]
    data_test = list(map(lambda x: tuple(x.split(' ')), data_test))
    data_test = [tuple(map(lambda x: float(x), item))
                 for item in data_test]


def sq_error_distortion(centers, data):

    result = 0
    n = len(data)
    for point in data:
        temp = distance_from_centers(centers, point) ** 2
        result += temp
    return round(result/n, 3)


print(sq_error_distortion(centers_test, data_test))
