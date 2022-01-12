def random_motifs_prob(num_seqs, gc_content, motif_seq):
    """probability that if num random DNA strings having the same length as s are constructed with GC-content,
    then at least one of the strings equals motif_seq.
    Input parameters are nums_seq in int, gc_content in float, motif_seq in str.
    Returns the probability in float number."""

    at_count = 0
    gc_count = 0
    for base in motif_seq:
        if base in "AT":
            at_count += 1
        else:
            gc_count += 1

    # Pr(at least one match of given num sequence = 1 - Pr(no match at all) = 1 - ((1-prob)**num_seq))
    prob = ((gc_content / 2) ** gc_count) * (((1 - gc_content) / 2) ** at_count)
    total_prob = 1 - ((1 - prob) ** num_seqs)
    return format(total_prob, ".3f")


with open("E:rosalind/rosalind_rstr.txt", "r") as f:
    temp = f.readline().strip().split(" ")
    num_seqs_test, gc_content_test = int(temp[0]), float(temp[1])
    motif_test = f.readline().strip()

print(random_motifs_prob(num_seqs_test, gc_content_test, motif_test))
