from math import log10


def random_strings(dna_string, gc_list):
    """get an array that represents the common logarithm of the probability
    that a random string constructed with the GC-content found in A[k] will match s exactly."""

    gc_count = 0
    at_count = 0
    for base in dna_string:
        if base in ["G", "C"]:
            gc_count += 1
        else:
            at_count += 1

    probabilities = []
    for gc in gc_list:
        prob = log10((((1 - gc) / 2) ** at_count) * (gc / 2) ** gc_count)
        prob = format(prob, ".3f")
        probabilities.append(prob)
    return probabilities


with open("E:rosalind/rosalind_prob.txt", "r") as f:
    string_test = f.readline().strip()
    gc_contents_test = f.readline().strip().split(" ")
    gc_contents_test = list(map(lambda x: float(x), gc_contents_test))

print(*random_strings(string_test, gc_contents_test))
