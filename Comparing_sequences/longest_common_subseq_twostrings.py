def lcs_backtrack(v, w):
    """Records which edge to compute s(i, j) by utilizing bractracking pointers"""
    s = []
    for i in range(len(v) + 1):
        s.append([])
        for j in range(len(w) + 1):
            s[i].append(0)

    backtrack = []
    for i in range(len(v)):
        backtrack.append([])
        for j in range(len(w)):
            backtrack[i].append(0)

    # for i in range(len(v)):
    #     s[i][0] = 0
    # for j in range(len(w)):
    #     s[0][j] = 0
    for i in range(1, len(v) + 1):
        for j in range(1, len(w) + 1):
            match = 0
            if v[i - 1] == w[j - 1]:
                match = 1
            s[i][j] = max(s[i - 1][j], s[i][j - 1], s[i - 1][j - 1] + match)
            if s[i][j] == s[i - 1][j]:
                backtrack[i - 1][j - 1] = '↓'
            elif s[i][j] == s[i][j - 1]:
                backtrack[i - 1][j - 1] = '→'
            elif s[i][j] == s[i - 1][j - 1] + match:
                backtrack[i - 1][j - 1] = '↘'
    return backtrack


# Using non recursive


# i index for v, j index for w, i and j is the index of the sink (last)
def output_lcs_(backtrack, v, i, j):
    """Returning a longest common subsequence"""
    output = ''
    if i == 0 and j == 0:
        return ''
    while i > 0 and j > 0:
        if backtrack[i - 1][j - 1] == '↘':
            output += v[i - 1]
            i -= 1
            j -= 1
        elif backtrack[i - 1][j - 1] == '↓':
            i -= 1
        else:
            j -= 1
    return output[::-1]


with open('E:/rosalind/rosalind_ba5c.txt', 'r') as f:
    seq1 = f.readline().strip()
    seq2 = f.readline().strip()
    seq1 = 'AACCTTGG'
    seq2 = 'ACACTGTGA'
    back_track = lcs_backtrack(seq1, seq2)
    print(output_lcs_(back_track, seq1, len(seq1), len(seq2)))
