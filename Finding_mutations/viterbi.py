from collections import defaultdict


def decoding_problem(emission_matrix, transition_matrix, states, emission_string):
    """Using Viterbi algorithm, find the path that maximizes the (unconditional) probability
    over all possible paths.
    input paramters are emisssion matrix (dict), transistion matrix (dict),
    states (list), and emission sequence in a string.
    Returns string most probable path."""

    initial_trans_prob = 1/len(states)
    backtrace = defaultdict(dict)
    score = defaultdict(dict)
    for i in range(len(emission_string)):
        for current_state in states:
            # start from the source
            if i == 0:
                score[current_state][i] = 1 * \
                    initial_trans_prob * \
                    emission_matrix[current_state][emission_string[i]]
                # print(str(i) + ': ' + 'source' + '>>' + current_state + ':\t' +
                #       '{:.5f}'.format(initial_trans_prob * emission_matrix[current_state + emission_string[i]]))

            else:
                score[current_state][i] = -float('inf')
                for state in states:
                    temp = score[state][i-1] * \
                        transition_matrix[state][current_state] * \
                        emission_matrix[current_state][emission_string[i]]
                    # print(str(i) + ': ' + state + '>>' + current_state + ':\t' + '{:.5f}'.format(
                    #     transition_matrix[state + current_state] * emission_matrix[current_state + emission_string[i]]))

                    if temp > score[current_state][i]:
                        score[current_state][i] = temp
                        backtrace[i][current_state] = state

    # Backtrace
    # Ambil state akhir dengan score yang paling tinggi
    max_score_state = max(
        score.keys(), key=lambda state: score[state][len(emission_string) - 1])

    max_prob_path = max_score_state
    current = max_score_state
    i = len(emission_string) - 1
    while i > 0:
        prev_state = backtrace[i][current]
        max_prob_path += prev_state
        current = prev_state
        i -= 1
    return max_prob_path[::-1]


with open('E:finding_mutations/dataset_26256_7.txt', 'r') as f:
    content = f.read().strip().split('--------')
    emision_string_test = content[0].strip()
    emission_symbols_test = content[1].strip().split(' ')
    states_test = content[2].strip().split(' ')
    temp0 = content[3].strip().split('\n')
    temp1 = temp0[0].split('\t')
    transition_matrix_test = defaultdict(dict)
    for i in range(len(states_test)):
        for j in range(len(states_test)):
            transition_matrix_test[states_test[i]][states_test[j]] = float(
                temp0[i+1].split('\t')[j+1])
    temp2 = content[4].strip().split('\n')
    temp3 = temp2[0].split('\t')

    emission_matrix_test = defaultdict(dict)
    for i in range(len(states_test)):
        for j in range(len(emission_symbols_test)):
            emission_matrix_test[states_test[i]][emission_symbols_test[j]] = float(
                temp2[i+1].split('\t')[j+1])

# print(decoding_problem(emission_matrix_test,
#       transition_matrix_test, states_test, emision_string_test))
