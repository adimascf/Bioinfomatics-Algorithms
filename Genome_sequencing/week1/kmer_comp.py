def kmer_composition(k, text):
    return [text[i:i+k] for i in range(0, len(text)-k+1)]


with open('E://problem_dna_sequencing/rosalind/rosalind_ba3a.txt') as f:
    len_kmer = f.readline().strip()
    sequence = f.read().strip()

for kmer in kmer_composition(int(len_kmer), sequence):
    print(kmer)
