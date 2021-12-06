
def first_and_last_column(text):
    """Create first and last column and stored in an array of tuples.
    input paramter is text that is produced by burrows wheeler transfrom"""

    base_count = {'A': 0, 'C': 0, 'T': 0, 'G': 0, '$': 0}
    last_column = []
    for b in text:
        base_count[b] += 1
        last_column.append((b, base_count[b]))
    first_column = sorted(last_column)
    return first_column, last_column


def last_to_first(first_column, last_column):
    """Create last to first index that store in an array.
    input parameter are first and last and column that stored in array of tuples
    return an array"""
    result = []
    curr_row = 0
    while len(result) != len(first_column):
        temp0 = last_column[curr_row]
        temp1 = first_column.index(temp0)
        result.append(temp1)
        curr_row += 1
    return result


def pattern_matching_bwt(last_column, pattern, last_to_first):
    """Using Borrws Wheeler Transform, finding the number of patter appear from a given text
    input paramters are last column (string that is produced by BWT), pattern string, and array of last to first
    return an integer"""

    pattern = list(map(lambda x: x, pattern))
    k = len(last_column)
    top = 0
    bottom = k - 1
    while top <= bottom:
        if len(pattern) > 0:
            symbol = pattern.pop()
            w = len(last_column[top:])
            temp = k - w
            if symbol in last_column[top:bottom+1]:
                top_idx = last_column[top:bottom+1].find(symbol) + temp
                bottom_idx = last_column[top:bottom+1].rfind(symbol) + temp
                top = last_to_first[top_idx]
                bottom = last_to_first[bottom_idx]

            else:
                return 0

        else:
            return bottom - top + 1


with open('E:finding_mutations/dataset_301_7.txt', 'r') as f:
    genome_test = f.readline().strip()
    patterns = f.read().strip().split(' ')

first, last = first_and_last_column(genome_test)
last_2_first = last_to_first(first, last)
for pattern in patterns:
    print(pattern_matching_bwt(genome_test, pattern, last_2_first), end=' ')
