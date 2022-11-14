#!/usr/bin/env python3
import sys


def sort_len_tot(alist):
    """Sort the contigs based their lenght and get the total length"""

    n = len(alist)
    tot = 0
    for i in range(n):
        for j in range(i+1, n):
            if len(alist[i]) < len(alist[j]):
                temp = alist[i]
                alist[i] = alist[j]
                alist[j] = temp
        tot += len(alist[i])
    return alist, tot


def main(contigs):
    """Get N50 and N75 for a collection of contigs"""

    sorted_contigs, tot_len = sort_len_tot(contigs)
    half, n50 = tot_len * 0.5, None
    three_q, n75 = tot_len * 0.75, None
    counter = 0
    check = False

    for contig in sorted_contigs:

        count_len = len(contig)
        counter += count_len
        if counter >= half and check == False:
            n50 = count_len
            check = True

        if counter >= three_q:
            n75 = count_len
            # break

    return n50, n75


with open(sys.argv[1], "r") as file:
    content = [contig.strip('\n') for contig in file.readlines()]
    print(sys.argv[1])
    print(*main(content))
