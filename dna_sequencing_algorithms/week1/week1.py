from matplotlib import pyplot as plt
import random


def longest_common_prefix(seq1, seq2):
    i = 0
    while i < len(seq1) and i < len(seq2) and \
        seq1[i] == seq2[i]:
        i += 1
    return seq1[:i]


# DOWNLOAD FILE

import urllib.request

url = 'http://d28rh4a8wq0iu5.cloudfront.net/ads1/data/phix.fa'
with urllib.request.urlopen(url) as f:
    fasta = f.read().decode('utf-8')

# WRITE DOWN INTO A FILE

with open('E:dna_seq/phix.fasta', 'w') as f:
    f.write(fasta)


def read_fasta(file_path):
    """reads fasta file parsing to dictionari in python"""

    with open(file_path, 'r') as f:
        contents = [line.strip() for line in f.readlines()]

    fasta = {}
    name = ''
    for line in contents:
        if '>' in line:
            name = line
            fasta[line] = ''
        else:
            fasta[name] += line

    return fasta


def counting_bases(seq):
    result = {'A': 0, 'G': 0, 'T': 0, 'C': 0}
    for base in seq:
        result[base] += 1
    return result


def read_fastq(file_path):
    """Reads fastq and parse it into sequences and
    qualities."""
    sequences = []
    qualities = []
    with open(file_path, 'r') as f:
        while True:
            name = f.readline()  # name, which read this is
            seq = f.readline().strip()  # seq line
            f.readline()  # + sign
            qual = f.readline().strip()
            if len(name) == 0:
                break
            sequences.append(seq)
            qualities.append(qual)

    return sequences, qualities


def phredd_33_toq(qual):
    """Converts quality simbol into ascii value and substract
    with 33"""
    return ord(qual) - 33


def create_histogram(qualities):
    """Creates histogram from qualitie values"""

    histogram_dict = {i: 0 for i in range(51)}  # value from 0 up to 50
    for qual in qualities:
        for phred in qual:
            q = phredd_33_toq(phred)
            histogram_dict[q] += 1

    x_value = list(histogram_dict.keys())
    y_value = list(histogram_dict.values())
    plt.bar(x_value, y_value)
    plt.xlabel("Quality scores")
    plt.ylabel("Frequency")
    # plt.yscale("log")
    plt.title("Quality scores fastq for SRR835775")
    plt.tight_layout()
    plt.show()


def find_gc_pos(reads):
    """Create line char show the distribution of gc content
    for each position in read."""
    gc = {i: 0 for i in range(100)}  # karena setiap read panjangnya seratus
    total = {i: 0 for i in range(100)}

    for read in reads:
        for i in range(len(read)):
            if read[i] == 'G' or read[i] == 'C':
                gc[i] += 1
            total[i] += 1

    for i in range(len(gc)):
        gc[i] = gc[i] / float(total[i])

    x_values = list(gc.keys())
    y_values = list(gc.values())
    plt.plot(x_values, y_values)
    plt.xlabel("Index positions")
    plt.ylabel("GC Contents")
    plt.title("GC Contents per index position")
    plt.tight_layout()
    # plt.xticks(x_values) # shows all x values
    plt.show()


def naive_pattern_search(pattern, genome):
    occurences = []
    for i in range(len(genome) - len(pattern) + 1):
        match = True
        for j in range(len(pattern)):
            if genome[i + j] != pattern[j]:
                match = False
                break
        if match:
            occurences.append(i)
    return occurences


def reverse_complement(sequence):
    complement = {'A': 'T', 'G': 'C', 'T': 'A', 'C': 'G', 'N': 'N'}
    result = ''
    for base in sequence:
        result = complement[base] + result
    return result


def generate_randreads(genome, num_reads, read_len):
    """Generate a list of reads from random position in the given
    genome"""

    reads = []
    len_genome = len(genome)
    for _ in range(num_reads):
        start = random.randint(0, (len_genome - read_len)) - 1
        reads.append(genome[start:start + read_len])
    return reads


def naive_with_mismatch(pattern, genome, m):
    """Naive search pattern with allowing m mismatch"""
    occurences = []
    for i in range(len(genome) - len(pattern) + 1):
        mismatch = 0
        for j in range(len(pattern)):
            if genome[i + j] != pattern[j]:
                mismatch += 1
                if mismatch > m:
                    break
        if mismatch <= m:
            occurences.append(i)
    return occurences