from shortest_superstring import read_fasta

complement_dna = {'A': 'T', 'G': 'C', 'T': 'A', 'C': 'G'}


def hamming_distance(seq1, seq2):
    """return number of difference char fro two same length string"""
    result = 0
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            result += 1
    return result


def complement_strand(seq):
    """for making the complement DNA strand"""
    result = ''
    for nuc in seq:
        result += complement_dna[nuc]
    return result


def reverse_complement(seq):
    """for reversing strand"""
    result = ''
    for nuc in seq:
        result += complement_dna[nuc]
    return result[::-1]


def error_correction(list_reads):
    """
    s was correctly sequenced and appears in the dataset at least twice (possibly as a reverse complement);
    s is incorrect, it appears in the dataset exactly once,
    and its Hamming distance is 1 with respect to exactly one correct read in the dataset (or its reverse complement).
    Input parameter is list of reads, returns dictionary {old: new}
    """
    result = {}
    rc_reads = [reverse_complement(read) for read in list_reads]
    total_reads = rc_reads + list_reads

    # correct and incorrect reads conatain distinct element
    correct_reads = set()
    incorrect_reads = set()
    for read in list_reads:
        if total_reads.count(read) > 1:
            correct_reads.add(read)
        elif total_reads.count(read) == 1:
            incorrect_reads.add(read)

    correct_reads = list(correct_reads)
    incorrect_reads = list(incorrect_reads)
    for i_read in incorrect_reads:

        # Hamming distance is 1 with respect to exactly one correct read in the dataset (or its reverse complement)
        count_hd, seq = 0, None
        count_hd_rc, rc_seq = 0, None

        for c_read in correct_reads:
            rc_read = reverse_complement(c_read)
            if hamming_distance(i_read, c_read) == 1:
                count_hd += 1
                seq = c_read

            elif hamming_distance(i_read, rc_read) == 1:
                count_hd_rc += 1
                rc_seq = rc_read

        if count_hd == 1:
            result[i_read] = seq

        elif count_hd_rc == 1:
            result[i_read] = rc_seq
    return result


# fasta_file = read_fasta('E:rosalind/rosalind_corr.txt')
# reads_test = list(fasta_file.values())
# for old, new in error_correction(reads_test).items():
#     print(old + '->' + new)
