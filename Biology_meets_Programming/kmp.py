def kmp_failure_arr(sequence):
    """Creates failure array of Knuth-Morris-Pratt algorithm from a given sequence of string
    The failure array of s is an array P of length n for which P[k] is the length of the longest substring s[j:k]
    that is equal to some prefix s[1:k-j+1], where j cannot equal 1 (otherwise, P[k] would always equal k).
    By convention, P[1]=0.
    Input string, returns a list of integer
    """
    seq_length = len(sequence)
    i = 0
    k = 1
    failure_arr = [0]
    while k < seq_length:
        if sequence[k] == sequence[i]:
            temp = i + 1
            failure_arr.append(temp)
            i += 1
            k += 1
        else:
            # i backward in failure array until i == 0 or sequence[i] == sequence[k]
            i = failure_arr[i - 1]
            while i != 0 and sequence[i] != sequence[k]:
                i = failure_arr[i - 1]

            if sequence[i] != sequence[k]:
                temp = 0
                failure_arr.append(temp)
                k += 1
    return failure_arr


with open("E:rosalind/rosalind_kmp.txt", "r") as f:
    f.readline()
    seq_test = ""
    content = f.readlines()
    for row in content:
        seq_test += row.strip()

print(*kmp_failure_arr(seq_test))
