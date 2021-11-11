from structures import DNA_Codons, complement_dna


def protein_translation2(dna_sequence):
    """Translates dna sequence into amino acid sequence"""
    aa_seq = ''
    for i in range(0, len(dna_sequence), 3):
        codon = dna_sequence[i:i+3]
        aa_seq += DNA_Codons[codon]
    return aa_seq


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


def peptide_encoding2(dna_seq, aa_seq):
    """Searching dna sequence that code a given amino acid sequence in six reading frames"""
    LEN_CODON = 3
    ldp = len(aa_seq) * LEN_CODON
    result = []

    for i in range(0, len(dna_seq) - ldp + 1):
        pattern = dna_seq[i:i+ldp]
        if protein_translation2(pattern) == aa_seq or protein_translation2(reverse_complement(pattern)) == aa_seq:
            result.append(pattern)
    return result


def main():
    with open('E:/rosalind/rosalind_ba4b.txt', 'r') as file:
        dna_sequence, aa_pattern = file.read().strip().split('\n')
        res = peptide_encoding2(dna_sequence, aa_pattern)
        for item in res:
            print(item)


if __name__ == '__main__':
    main()
