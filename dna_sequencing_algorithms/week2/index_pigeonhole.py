def pigeonhole_approximate_matching(pattern, genome, index, n):
    """Implement the pigeonhole principle using Index object to find approximate
    matches for the partitions with maximum n mismatches."""

    segment_length = int(round(len(pattern) / (n + 1)))
    all_matches = set()
    k = index.k
    index_hits = set()
    for i in range(n + 1):
        start = i * segment_length
        end = start + k
        matches = index.query(pattern[start:end])
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
