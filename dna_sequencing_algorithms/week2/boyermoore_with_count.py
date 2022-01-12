def bm_with_counts(pattern, p_bm, genome):
    """implement versions of the Boyer-Moore algorithms that additionally count and return
    (a) the number of character comparisons performed and (b) the number of alignments tried"""

    i = 0
    occurences = []
    num_alignments = 0
    num_char_comparisions = 0
    k = 0
    while i < len(genome) - len(pattern) + 1:
        shift = 1
        mismatched = False
        num_alignments += 1

        for j in range(len(pattern) - 1, -1, -1):
            num_char_comparisions += 1
            if genome[i + j] != pattern[j]:
                skip_bc = p_bm.bad_character_rule(j, genome[i + j])
                skip_gs = p_bm.good_suffix_rule(j)
                shift = max(shift, skip_bc, skip_gs)
                mismatched = True
                i += shift - 1
                break
            else:
                k += 1

        if mismatched == False:
            occurences.append(i)
            skip_gs = p_bm.match_skip()
            shift = max(shift, skip_gs)
            i += shift - 1
        i += 1
    return occurences, num_alignments, num_char_comparisions
