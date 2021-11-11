def manhattan_tourist(n, m, down, right):
    """The length of a longest path from source (0, 0) to sink (n, m)
    in the rectangular grid whose edges are defined by the matrices Down and Right."""

    # Create matrix array. I use nested list. list with length m+1 and amount n+1
    s = []
    for i in range(n+1):
        # Append an empty sublist inside the list
        s.append([])
        for j in range(m+1):
            s[i].append(0)

    s[0][0] = 0
    for i in range(1, n+1):
        s[i][0] = s[i-1][0] + down[i-1][0]
    for j in range(1, m+1):
        s[0][j] = s[0][j-1] + right[0][j-1]
    for i in range(1, n+1):
        for j in range(1, m+1):
            s[i][j] = max(s[i-1][j] + down[i-1][j], s[i][j-1] + right[i][j-1])
    return s[n][m]


with open('E:/rosalind/rosalind_ba5b.txt', 'r') as f:
    file = f.readlines()
    lines = [line.rstrip() for line in file]
    [n, m] = [int(e) for e in lines[0].split()]
    b = lines.index('-')
    down, right = lines[1:b], lines[b+1:]
    down = [[int(e) for e in E.split()] for E in down]
    right = [[int(e) for e in E.split()] for E in right]

print(manhattan_tourist(n, m, down, right))
