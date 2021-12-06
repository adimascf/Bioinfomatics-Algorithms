from collections import defaultdict


def parse_state(state):
    """Parse state string and integer
    """
    s_symbol = state[0]
    s_idx = state[1:]
    if s_symbol == 'S':
        s_idx = 0

    if s_idx != '':
        return s_symbol, int(s_idx)
    else:
        return s_symbol, -1


def is_valid(state1, state2, end_idx):
    """Check whether the transition is valid or not
    in the HMM profile graph.
    """

    state1, state2 = [parse_state(s) for s in (state1, state2)]

    if state2[0] == 'E':
        if state1[0] + str(state1[1]) in [s + str(end_idx) for s in ['M', 'I', 'D']]:
            return True

    if state1[0] != 'E':
        if state2[0] + str(state2[1]) in ['D' + str(state1[1] + 1), 'M' + str(state1[1] + 1), 'I' + str(state1[1])]:
            return True

    return False


def pseudocount_HHM_profile(alignment, symbols, insertion_threshold, pseudocount=0.01):
    """ Construct a profile HMM with pseudocount from a multiple alignment.
    Input parameters are a list of sequences alignment, a list of symbols, floating number of threshold.
    Return transition and emission matrix in dictionary"""

    # Remove column if the insertion fraction exceeds the threshold
    columns_idxs = []
    for i in range(len(alignment[0])):
        col = []
        for j in range(len(alignment)):
            col.append(alignment[j][i])
        temp = sum(x == '-' for x in col)/len(col)
        if temp <= insertion_threshold:
            columns_idxs.append(i)

    # Determines all possible states
    all_states = ['S', 'I0']
    for i in range(len(columns_idxs)):
        all_states.append('M' + str(i+1))
        all_states.append('D' + str(i+1))
        all_states.append('I' + str(i+1))
    all_states.append('E')

    # CALCULATES THE TRANSITION PROBABILITIES
    # Initializes the transitions value matrix
    num_transitions = defaultdict(dict)
    for s1 in all_states:
        for s2 in all_states:
            num_transitions[s1][s2] = 0

    for current_seq in alignment:
        current_state = 'S'
        col_idx = 0

        while current_state != 'E':
            # Determines state index
            if current_state == 'S':
                curr_state_idx = 0
            else:
                curr_state_idx = int(current_state[1:])

            # DETERMINES THE NEXT STATE
            next_state = current_state  # for initializing the next_state
            # end state
            if col_idx == len(current_seq):
                next_state = 'E'

            elif col_idx in columns_idxs:

                # Match
                if current_seq[col_idx] != '-':
                    next_state = 'M' + str(curr_state_idx + 1)

                # Deletion
                else:
                    next_state = 'D' + str(curr_state_idx + 1)

            # Insertion
            elif col_idx not in columns_idxs and current_seq[col_idx] != '-':
                next_state = 'I' + str(curr_state_idx)

            # Pass deletion in non-included columns indexes
            if next_state != current_state or (current_state.startswith('I') and current_seq[col_idx] != '-'):
                num_transitions[current_state][next_state] += 1
                current_state = next_state

            col_idx += 1

    raw_transition_matrix = defaultdict(dict)
    for state1, row in num_transitions.items():
        row_total_val = sum(row.values())
        for state2, val in row.items():
            if row_total_val != 0:
                raw_transition_matrix[state1][state2] = val / row_total_val
            else:
                raw_transition_matrix[state1][state2] = val

    # Add pseudocount and normalize
    transition_matrix = defaultdict(dict)
    end_index = len(columns_idxs)
    for state1, row in raw_transition_matrix.items():

        # Calculate normalize factor
        norm_factor = 0
        for state2 in all_states:
            if is_valid(state1, state2, end_index):
                norm_factor += row[state2] + pseudocount

        # Add pseudocount
        for state2, val in row.items():
            if is_valid(state1, state2, end_index):
                transition_matrix[state1][state2] = (
                    val + pseudocount) / norm_factor
            else:
                transition_matrix[state1][state2] = val
    # EMISSION PROBABILTY
    # Initializes emission num matrix with all value 0
    num_emissions = defaultdict(dict)
    for state in all_states:
        for symbol in symbols:
            num_emissions[state][symbol] = 0

    for current_seq in alignment:
        current_state = 'S'
        col_idx = 0

        while current_state != 'E':

            # Determines state index
            if current_state == 'S':
                curr_state_idx = 0
            else:
                curr_state_idx = int(current_state[1:])

            # DETERMINES THE NEXT STATE

            # End state
            if col_idx == len(current_seq):
                next_state = 'E'

            elif col_idx in columns_idxs:
                # Match
                if current_seq[col_idx] != '-':
                    next_state = 'M' + str(curr_state_idx + 1)

                # Deletion
                else:
                    next_state = 'D' + str(curr_state_idx + 1)

            # Insertion
            elif col_idx not in columns_idxs and current_seq[col_idx] != '-':
                next_state = 'I' + str(curr_state_idx)

            # Pass deletion in non-included column
            if next_state != 'E':
                temp = current_seq[col_idx]
                if next_state != current_state or (current_state.startswith('I') and temp != '-'):
                    if temp != '-':
                        num_emissions[next_state][temp] += 1
            current_state = next_state
            col_idx += 1

    raw_emission_matrix = defaultdict(dict)
    for state, row in num_emissions.items():
        row_total_val = sum(row.values())
        for symbol, val in row.items():
            if row_total_val != 0:
                raw_emission_matrix[state][symbol] = val / row_total_val
            else:
                raw_emission_matrix[state][symbol] = val

    # Add pseudocount and normalize
    emission_matrix = defaultdict(dict)
    end_index = len(columns_idxs)
    for state, row in raw_emission_matrix.items():
        if state not in ['S', 'E'] and not state.startswith('D'):
            # Calculate normalization factor
            norm_factor = 0
            for val in row.values():
                norm_factor += val + pseudocount

            # Add pseudocount to value matrix and normalize it
            for symbol, val in row.items():
                emission_matrix[state][symbol] = (
                    val + pseudocount) / norm_factor

        else:
            for symbol, val in row.items():
                emission_matrix[state][symbol] = val

    return transition_matrix, emission_matrix


def output_format(*dictionary_result, separated='\t'):
    """Build matrix-like format from dictionary format"""

    for i, matrix in enumerate(dictionary_result):
        row_labels = list(matrix.keys())
        col_labels = list(matrix[row_labels[0]].keys())

        if i == 0:
            to_print = separated + separated.join(col_labels) + '\t\n'
        else:
            to_print = separated + separated.join(col_labels) + '\n'

        for r_label in row_labels:
            temp = [r_label]
            for c_label in col_labels:
                val = matrix[r_label][c_label]
                if val == 0:
                    val_str = '0'
                elif val == int(val):
                    val_str = str(format(val, '.1f'))
                else:
                    val_str = str(format(val, '.3f')).rstrip('0')
                temp.append(val_str)

            to_print += separated.join(temp)
            if r_label != row_labels[-1]:
                to_print += '\n'

        print(to_print)
        if i == 0:
            print('--------')

    return


with open('E:finding_mutations/dataset_26259_5.txt', 'r') as f:
    temp = f.readline().strip().split(' ')
    threshold_test, pseudocount_test = float(temp[0]), float(temp[1])
    f.readline()
    symbols_test = f.readline().strip().split(' ')
    f.readline()
    alignment_test = f.readlines()
    alignment_test = list(map(lambda x: x.strip(), alignment_test))

# trans, emis = pseudocount_HHM_profile(
#     alignment_test, symbols_test, threshold_test, pseudocount_test)
# output_format(trans, emis)
