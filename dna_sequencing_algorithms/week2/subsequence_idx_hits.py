def subseq_approximate_matching(pattern, genome, index, n):
    """Implement the pigeonhole principle using Index subsequence object to find approximate
    matches for the partitions with maximum n mismatches."""

    segment_length = int(round(len(pattern) / (n + 1)))
    all_matches = set()
    k = index.k
    index_hits = 0

    for i in range(n + 1):
        print(i)
        matches = index.query(pattern[i:])
        index_hits += len(matches)

        for m in matches:
            text_offsets = m - i
            if text_offsets < 0 or (text_offsets + len(pattern)) > len(genome):
                continue

            mismatches = 0
            for j in range(0, len(pattern)):
                if pattern[j] != genome[text_offsets + j]:
                    mismatches += 1
                    if mismatches > n:
                        break

            if mismatches <= n:
                all_matches.add(text_offsets)
    return list(all_matches), index_hits
