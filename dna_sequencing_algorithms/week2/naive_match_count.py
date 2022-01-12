def naive_with_counts(pattern, genome):
    """implement versions of the naive exact matching that additionally count and return
    (a) the number of character comparisons performed and (b) the number of alignments tried"""
    occurences = []
    num_alignment = 0
    num_char_comparisions = 0
    for i in range(len(genome) - len(pattern) + 1):
        num_alignment += 1
        match = True
        for j in range(len(pattern)):
            num_char_comparisions += 1
            if genome[i + j] != pattern[j]:
                match = False
                break
        if match:
            occurences.append(i)
    return occurences, num_alignment, num_char_comparisions
