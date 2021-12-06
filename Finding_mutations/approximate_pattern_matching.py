from burrows_wheeler import burrows_wheeler_tranform
from multiple_pattern_matching import create_check_point, count_symbol, bwt_matching, first_occurance
from suffix_array import partial_suffix_array


def pattern_to_seeds(pattern, d):

    min_size = len(pattern) // (d+1)
    cut_points = list(range(0, len(pattern) - min_size + 1, min_size))
    cut_points.append(len(pattern))

    seeds = []
    offsets = []
    for i in range(1, len(cut_points)):
        seeds.append(pattern[cut_points[i-1]:cut_points[i]])
        offsets.append(cut_points[i-1])
    return seeds, offsets


def seed_positions(seed, first_occurance, bwt_string, check_point, partial_suffix_array):

    result = []
    top, bottom = bwt_matching(first_occurance, bwt_string, seed, check_point)
    if top:
        for i in range(top, bottom+1):
            to_add = 0
            while i not in partial_suffix_array.keys():
                i = first_occurance[bwt_string[i]] + \
                    count_symbol(check_point, i, bwt_string, bwt_string[i])
                to_add += 1
            result.append(partial_suffix_array[i] + to_add)
    return result


def multiple_approximate_pattern_matching(genome, patterns, d, c):

    bwt_string = burrows_wheeler_tranform(genome + '$')
    fo = first_occurance(bwt_string)
    check_point = create_check_point(bwt_string, c)
    partial_sufix_arr = partial_suffix_array(genome + '$', c)

    positions = {}
    for pattern in patterns:
        # Break pattern into seeds
        seeds, offsets = pattern_to_seeds(pattern, d)

        # Find exact matches and try to extend each seed
        pattern_pos_list = set()
        for candidate_seed, offset in zip(seeds, offsets):
            seed_pos = seed_positions(
                candidate_seed, fo, bwt_string, check_point, partial_sufix_arr)

            for candidate_pos in seed_pos:
                pattern_pos = candidate_pos - offset

                if pattern_pos >= 0 and pattern_pos + len(pattern) <= len(genome):
                    approximate_match_flag = True
                    num_mismatch = 0
                    for i, symbol in enumerate(pattern):
                        if symbol != genome[pattern_pos+i]:
                            num_mismatch += 1
                            if num_mismatch > d:
                                approximate_match_flag = False
                                break
                    if approximate_match_flag:
                        pattern_pos_list.add(pattern_pos)
        positions[pattern] = sorted(list(pattern_pos_list))
    return positions


with open('E:finding_mutations/dataset_304_10.txt', 'r') as f:
    genome_test = f.readline().strip()
    patterns_test = f.readline().strip().split(' ')
    d_test = int(f.readline().strip())

    result = multiple_approximate_pattern_matching(
        genome_test, patterns_test, d_test, c=100)
    for k, v in result.items():
        print(k + ':', end=' ')
        print(*v)
