with open('E://problem_dna_sequencing//blosum62.txt', 'r') as f:
    content_list = [line.strip() for line in f.readlines()]
    amino_acids = content_list[0].split()
    blosum62 = {}
    for i in range(len(amino_acids)):
        for j in range(len(amino_acids)):
            blosum62[amino_acids[i] + amino_acids[j]
                     ] = int(content_list[i+1].split()[j+1])


def efficient_scoring(v, w, sigma=5):
    """Creates two column and find maximum score for connecting their nodes"""

    v = "-" + v
    w = "-" + w
    s_current = [0] * len(v)
    for i in range(1, len(v)):
        s_current[i] = s_current[i-1] - sigma

    for j in range(1, len(w)):
        s_next = [-sigma * j] * len(v)
        for i in range(1, len(v)):
            key = v[i] + w[j]

            s_next[i] = max(s_current[i-1] + blosum62[key],
                            s_next[i-1] - sigma, s_current[i] - sigma)
        s_current = s_next

    return s_current


def middle_edge(v, w, top=0, bottom=None, left=0, right=None):
    """Find edges in the middle of the matrix whoch connect two nodes from source to sink"""

    if bottom is None:
        bottom = len(v)
    if right is None:
        right = len(w)
    mid_col = (right+left) // 2

    from_scource1 = efficient_scoring(v[top:bottom], w[left:mid_col])
    to_sink1 = efficient_scoring(
        v[top:bottom][::-1], w[mid_col:right][::-1])[::-1]

    max_len = -1e6
    for i in range(len(from_scource1)):
        current = from_scource1[i] + to_sink1[i]
        if current > max_len:
            max_len = current
            idx1 = i

    from_scource2 = efficient_scoring(v[top:bottom], w[left:mid_col+1])
    to_sink2 = efficient_scoring(
        v[top:bottom][::-1], w[mid_col+1:right][::-1])[::-1]

    max_len = -1e6
    for i in range(len(from_scource2)):
        current = from_scource2[i] + to_sink2[i]
        if current > max_len:
            max_len = current
            idx2 = i

    if idx2 == idx1 + 1:
        return '↘', (idx1 + top, mid_col), (idx1 + top + 1, mid_col + 1)
    elif idx2 == idx1:
        return '→', (idx1 + top, mid_col), (idx1 + top, mid_col + 1)
    else:
        return '↓', (idx1 + top, mid_col), (idx1 + top + 1, mid_col)


def alignment_score(v, w, sigma=5):
    """Scoring two string that already aligned"""
    score = 0
    for i in range(len(v)):
        if v[i] == '-' or w[i] == '-':
            score -= sigma
        else:
            score += blosum62[v[i] + w[i]]
    return score


def linear_space_alignment(v, w, top=0, bottom=None, left=0, right=None):
    """Linear Space Alignment to solve the Global Alignment Problem for a large dataset"""
    if bottom is None:
        bottom = len(v)
    if right is None:
        right = len(w)

    if left == right:
        return '↓' * (bottom-top)
    if top == bottom:
        return '→' * (right-left)

    mid_edge, mid_from, mid_to = middle_edge(v, w, top, bottom, left, right)
    print(mid_from, mid_to)
    # left
    row, column = mid_from
    path_left = linear_space_alignment(v, w, top, row, left, column)

    # right
    row, column = mid_to
    path_right = linear_space_alignment(v, w, row, bottom, column, right)
    return path_left + mid_edge + path_right


def backtracking(path, v, w):
    aligned1 = ''
    aligned2 = ''
    i = 0
    j = 0
    for arrow in path:
        if arrow == '↘':
            aligned1 += v[i]
            aligned2 += w[j]
            i += 1
            j += 1
        elif arrow == '↓':
            aligned1 += v[i]
            aligned2 += '-'
            i += 1
        else:
            aligned1 += '-'
            aligned2 += w[j]
            j += 1

    return aligned1, aligned2


if __name__ == "__main__":

    with open('E:rosalind//rosalind_ba5k.txt', 'r') as file:
        s1 = file.readline().strip()
        s2 = file.readline().strip()
    path = linear_space_alignment(s1, s2)

    alignment1, alignment2 = backtracking(path, s1, s2)

    print(alignment_score(alignment1, alignment2))
    print(alignment1)
    print(alignment2)
