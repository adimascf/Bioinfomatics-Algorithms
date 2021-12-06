from burrows_wheeler import burrows_wheeler_tranform
from suffix_array import partial_suffix_array
from better_bwt_matching import first_occurance


def create_check_point(bwt_string, c):

    unique_char = list(set(bwt_string))
    check_point = {}
    for i in range(0, len(bwt_string), c):
        check_point[i] = {}
        for char in unique_char:
            check_point[i][char] = bwt_string[:i].count(char)
    return check_point


def count_symbol(check_point, idx, bwt_string, character):

    keys = [key for key in check_point.keys() if key <= idx]
    nearest_idx = min(keys, key=lambda x: abs(x-idx))

    count = check_point[nearest_idx][character]
    count += bwt_string[nearest_idx:idx].count(character)
    return count


def bwt_matching(first_occurance, bwt_string, pattern, check_point):
    """Using check points count, find position top and bottom BWT matching.
    input parameters are dict first occurance (dict), string BWT(text), pattern string, check point(dict).
    Returns False, False if the pattern doesn't appear. If appears, returns integer of idx top and bottom."""

    pattern = list(map(lambda x: x, pattern))
    k = len(bwt_string)
    top = 0
    bottom = k - 1
    while top <= bottom:
        if len(pattern) > 0:
            symbol = pattern.pop()

            if symbol in bwt_string[top:bottom+1]:
                top = first_occurance[symbol] + \
                    count_symbol(check_point, top, bwt_string, symbol)
                bottom = first_occurance[symbol] + \
                    count_symbol(check_point, bottom+1, bwt_string, symbol) - 1
            else:
                return False, False
        else:
            return top, bottom


def multiple_patterns_matching(genome, patterns, c=5):
    """Using modified BWT matching above, finds the index of the first character of the patterns, if matched.
    Input parameters are string of the text, a list of patterns, and number of check point (int)"""

    bwt_string = burrows_wheeler_tranform(genome + '$')
    fo = first_occurance(bwt_string)
    check_point = create_check_point(bwt_string, c)
    partial_suffix = partial_suffix_array(genome + '$', c)

    first_pos = {}
    for pattern in patterns:
        pos = []
        top, bottom = bwt_matching(fo, bwt_string, pattern, check_point)
        if top:
            for i in range(top, bottom+1):
                add = 0
                while i not in partial_suffix.keys():
                    i = fo[bwt_string[i]] + \
                        count_symbol(check_point, i, bwt_string, bwt_string[i])
                    add += 1
                pos.append(partial_suffix[i] + add)
        pos = sorted(pos)
        first_pos[pattern] = pos

    return first_pos


# with open('E:finding_mutations/dataset_303_4.txt', 'r') as f:
#     first_column_test = f.readline().strip()
#     patterns = f.read().strip().split(' ')
#     print(len(first_column_test), len(patterns))
#     for key, val in multiple_patterns_matching(first_column_test, patterns, 100).items():
#         print(key + ':', end=' ')
#         print(*val)
