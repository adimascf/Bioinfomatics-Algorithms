def k_reversal(p, k):
    """making reversal"""
    j = k
    while p[j] != k+1 and p[j] != -(k+1):
        j += 1

    p[k:j+1] = list(map(lambda x: -x, p[k:j+1][::-1]))
    return p


def greedy_sorting(p):
    """p is unsorting array"""
    result = []
    for k in range(len(p)):
        while p[k] != k + 1:
            p = k_reversal(p, k)
            result.append(list(p))

    return result


with open('E://rosalind//rosalind_ba6a.txt', 'r') as f:
    contents = f.read().strip()
    temp = contents[1:-1].split(' ')
    test = list(map(lambda x: int(x), temp))

reversal = greedy_sorting(test)
for step in reversal:
    for i in range(len(step)):
        if step[i] > 0:
            step[i] = '+' + str(step[i])
        else:
            step[i] = str(step[i])
    print('(' + ' '.join(step)+')')
