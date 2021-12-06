from burrows_wheeler import burrows_wheeler_tranform


def count_array(bwt_string):

    result = []
    i = 0
    k = len(bwt_string) + 1
    while i != k:
        count = {'$': 0, 'A': 0, 'C': 0, 'T': 0, 'G': 0}
        for char in bwt_string[:i]:
            count[char] += 1
        result.append(dict(count.items()))
        count.clear()
        i += 1

    return result


def first_occurance(bwt_string):
    """Find the indexes of each character's occurance in first column"""
    result = {'$': 0, 'A': 0, 'C': 0, 'T': 0, 'G': 0}
    bwt_string = ''.join(sorted(bwt_string))
    for item in result:
        result[item] = bwt_string.find(item)
    return result


def better_matching_bwt(first_occurance, last_column, pattern, count):
    """Using (better) Borrws Wheeler Transform, finding the number of patter appear from a given text
    input paramters are last column (string that is produced by BWT), pattern string, and array of last to first
    return an integer"""

    pattern = list(map(lambda x: x, pattern))
    k = len(last_column)
    top = 0
    bottom = k - 1
    while top <= bottom:
        if len(pattern) > 0:
            symbol = pattern.pop()
            if symbol in last_column[top:bottom+1]:
                top = first_occurance[symbol] + count[top][symbol]
                bottom = first_occurance[symbol] + count[bottom+1][symbol] - 1

            else:
                return 0

        else:
            return bottom - top + 1


# with open('E:finding_mutations/dataset_301_7.txt', 'r') as f:
#     first_column_test = f.readline().strip()
#     patterns = f.read().strip().split(' ')
#     last_column_test = burrows_wheeler_tranform(first_column_test)
#     fo_test = first_occurance(last_column_test)
#     count_test = count_array(last_column_test)
#     # for pattern in patterns:
#     #     print(better_matching_bwt(
#     #         fo_test, last_column_test, pattern, count_test), end=' ')
