import pickle
import numpy as np
import matplotlib.pyplot as plt

def append_to_pickle(file_path, data):
    with open(file_path, 'ab') as f:  # Open file in binary append mode
        for d in data:
            pickle.dump(d, f)


def read_pickle(file_path):
    data = []
    with open(file_path, 'rb') as f:  # Open file in binary read mode
        while True:
            try:
                item = pickle.load(f)
                data.append(item)
            except EOFError:
                break
    return data

def build_graph(data):
        # Assign sample IDs based on order of appearance for each island ID
    sample_id_mapping = {}
    for d in data:
        island_id = d['Island ID']
        if island_id not in sample_id_mapping:
            sample_id_mapping[island_id] = 1
        d['Sample_id'] = sample_id_mapping[island_id]
        sample_id_mapping[island_id] += 1

    # Initialize matrix to store scores for each island ID
    max_samples = max (sample_id_mapping.values())
    num_islands = max(d['Island ID'] for d in data if d['Island ID'] is not None) + 1
    score_matrix = np.zeros((num_islands, max_samples))
    score_matrix = score_matrix[:, :] + 2048

    # Fill the score matrix with scores based on island ID and new sample id
    for d in data:
        if d['Island ID'] is not None:
            score_matrix[d['Island ID'], d['Sample_id']] = d['Score']

    # Plotting
    plt.figure(figsize=(10, 6))

    for island_id in range(num_islands):
        plt.plot(range(max_samples), score_matrix[island_id], label=f'Island {island_id}')

    plt.xlabel('Sample ID')
    plt.ylabel('Score')
    plt.title('Scores per Sample ID for Each Island')
    plt.legend()
    plt.grid(True)
    plt.show()

def build_graph1(data):
        # Assign sample IDs based on order of appearance for each island ID


    # Initialize matrix to store scores for each island ID
    max_samples = max(d['Sample_num'] for d in data) + 1
    num_islands = max(d['Island ID'] for d in data if d['Island ID'] is not None) + 1
    score_matrix = np.zeros((num_islands, max_samples))
    score_matrix = score_matrix[:, :] + 2048

    # Fill the score matrix with scores based on island ID and new sample id
    for d in data:
        if d['Island ID'] is not None:
            score_matrix[d['Island ID'], d['Sample_num']] = d['Score']

    # Plotting
    plt.figure(figsize=(10, 6))

    for island_id in range(num_islands):
        plt.plot(range(max_samples), score_matrix[island_id], label=f'Island {island_id}')

    plt.xlabel('Sample ID')
    plt.ylabel('Score')
    plt.title('Scores per Sample ID for Each Island')
    plt.legend()
    plt.grid(True)
    plt.show()

# Example usage:
# file_path = "scores.pickle"
# data_to_append = {"Island ID": 1, "Score": 0.8}  # Example data to append
# append_to_pickle(file_path, data_to_append)


# Example usage:
# file_path = "scores/scores3.pickle"
# data = read_pickle(file_path)
# print(data)
# build_graph(data)

new_file_path = 'scores/15Island10Iteration.pickle'
data = read_pickle(new_file_path)
print(data)
build_graph(data)
# islands = {'Sample_num': 3, 'Island ID': 0, 'Score': 2048}, {'Sample_num': 2, 'Island ID': 0, 'Score': 2220}, {'Sample_num': 3, 'Island ID': 0, 'Score': 2048}, {'Sample_num': 2, 'Island ID': 0, 'Score': 2168}, {'Sample_num': 3, 'Island ID': 0, 'Score': 2048}, {'Sample_num': 3, 'Island ID': 0, 'Score': 2048}, {'Sample_num': 2, 'Island ID': 0, 'Score': 2048}, {'Sample_num': 3, 'Island ID': 0, 'Score': 2202}, {'Sample_num': 3, 'Island ID': 0, 'Score': 2048}, {'Sample_num': 2, 'Island ID': 0, 'Score': 2285}, {'Sample_num': 3, 'Island ID': 0, 'Score': 2328}, {'Sample_num': 5, 'Island ID': 0, 'Score': 2231}, {'Sample_num': 4, 'Island ID': 0, 'Score': 2448}, {'Sample_num': 4, 'Island ID': 0, 'Score': 2048}, {'Sample_num': 5, 'Island ID': 0, 'Score': 2304}, {'Sample_num': 4, 'Island ID': 0, 'Score': 2048}, {'Sample_num': 5, 'Island ID': 0, 'Score': 2048}, {'Sample_num': 4, 'Island ID': 0, 'Score': 2048}, {'Sample_num': 4, 'Island ID': 0, 'Score': 2448}, {'Sample_num': 4, 'Island ID': 0, 'Score': 2310}, {'Sample_num': 5, 'Island ID': 0, 'Score': 2048}, {'Sample_num': 7, 'Island ID': 0, 'Score': 2048}, {'Sample_num': 7, 'Island ID': 0, 'Score': 2429}, {'Sample_num': 6, 'Island ID': 0, 'Score': 2048}, {'Sample_num': 7, 'Island ID': 0, 'Score': 2048}, {'Sample_num': 7, 'Island ID': 0, 'Score': 2340}, {'Sample_num': 7, 'Island ID': 0, 'Score': 2386}, {'Sample_num': 7, 'Island ID': 0, 'Score': 2190}, {'Sample_num': 9, 'Island ID': 0, 'Score': 2788}, {'Sample_num': 8, 'Island ID': 0, 'Score': 2686}, {'Sample_num': 9, 'Island ID': 0, 'Score': 2788}, {'Sample_num': 8, 'Island ID': 0, 'Score': 2048}, {'Sample_num': 9, 'Island ID': 0, 'Score': 2048}, {'Sample_num': 8, 'Island ID': 0, 'Score': 2788}, {'Sample_num': 8, 'Island ID': 0, 'Score': 2788}, {'Sample_num': 9, 'Island ID': 0, 'Score': 2048}, {'Sample_num': 8, 'Island ID': 0, 'Score': 2048}, {'Sample_num': 8, 'Island ID': 0, 'Score': 2048}, {'Sample_num': 8, 'Island ID': 0, 'Score': 2518}, {'Sample_num': 9, 'Island ID': 0, 'Score': 2067}, {'Sample_num': 9, 'Island ID': 0, 'Score': 2505}

# append_to_pickle(new_file_path, islands)

