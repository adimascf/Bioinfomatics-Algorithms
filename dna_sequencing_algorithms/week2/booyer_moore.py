from bm_preproc import BoyerMoore


def boyer_more(pattern, p_bm, genome):
    """Implement Bayer Moore object for pattern searchingh."""

    i = 0
    occurences = []
    while i < len(genome) - len(pattern) + 1:
        shift = 1
        mismatched = False
        for j in range(len(pattern) - 1, -1, -1):
            if genome[i + j] != pattern[j]:
                skip_bc = p_bm.bad_character_rule(j, genome[i + j])
                skip_gs = p_bm.good_suffix_rule(j)
                shift = max(shift, skip_bc, skip_gs)
                mismatched = True
                break
        if mismatched == False:
            occurences.append(i)
            skip_gs = p_bm.match_skip()
            shift = max(shift, skip_gs)
        i += 1

    return occurences


def approximate_matching(pattern, genome, n):
    """With boyer moore algorithm, find aproximate matching
    with maximum n mismatches."""

    segment_length = int(round(len(pattern) / (n + 1)))
    all_matches = set()
    index_hits = set()
    for i in range(n + 1):
        start = i * segment_length
        end = min((i + 1) * segment_length, len(pattern))

        try:
            p_bm = BoyerMoore(pattern[start:end], alphabet="ACGT")
        except AssertionError:
            return "AssertionError: The suffix pattern length is less than two. Minimize the number of max mismatch."

        matches = boyer_more(pattern[start:end], p_bm, genome)
        set_matches = set(matches)
        index_hits = index_hits.union(set_matches)

        for m in matches:
            if m < start or m - start + len(pattern) > len(genome):
                continue

            mismatches = 0
            for j in range(0, start):
                if pattern[j] != genome[m - start + j]:
                    mismatches += 1
                    if mismatches > n:
                        break

            for j in range(end, len(pattern)):
                if pattern[j] != genome[m - start + j]:
                    mismatches += 1
                    if mismatches > n:
                        break

            if mismatches <= n:
                all_matches.add(m - start)
    print(f"Index hits: {len(index_hits)}")
    return list(all_matches)
