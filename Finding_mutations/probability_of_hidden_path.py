def hidden_path_prob(hidden_path, states, transisiton_matrix):
    """Calculates the probability from a given hidden path string.
    Input paramters are string of hidden path, a list of states, adn transition matrix in dictionary.
    Returns floating number of probability."""

    initial_prob = 1/len(states)
    probability = initial_prob
    temp = None
    for state in hidden_path:
        if temp == None:
            temp = state
        else:
            probability *= transisiton_matrix[temp+state]
            temp = state
    return probability


with open('E:finding_mutations/dataset_26255_8.txt', 'r') as f:
    content = f.read().strip().split('--------')
    hidden_path_test = content[0].strip()
    states_test = content[1].replace('\n', '').split(' ')
    temp = content[2].strip().split('\n')
    print(temp)
    temp1 = temp[0].split('\t')
    print(temp1)
    matrix_test = {}
    for i in range(len(temp1)):
        for j in range(len(temp1)):
            matrix_test[temp1[i]+temp1[j]] = float(temp[i+1].split('\t')[j+1])

print(hidden_path_prob(hidden_path_test, states_test, matrix_test))
