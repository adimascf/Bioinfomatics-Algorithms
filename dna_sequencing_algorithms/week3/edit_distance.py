def edit_distance(seq1, seq2, epilson=1):

    k1, k2 = len(seq1), len(seq2)
    s = [[0 for _ in range(k2+1)] for _ in range(k1+1)]
    for i in range(k1+1):
        s[i][0] = epilson * i
    for i in range(k2+1):
        s[0][i] = epilson * i

    for i in range(1, k1+1):
        for j in range(1, k2+1):
            delta = 1 if seq1[i-1] != seq2[j-1] else 0

            s[i][j] = min(s[i-1][j-1] + delta, s[i-1][j] + epilson,
                          s[i][j-1] + epilson)
    return s[-1][-1]


x = 'Shakespeare'
y = 'shake spear'

print(edit_distance(x, y))
