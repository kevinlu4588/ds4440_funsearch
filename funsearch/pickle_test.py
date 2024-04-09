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

new_file_path = 'scores/5Island10Iteration.pickle'
data = read_pickle(new_file_path)
print(data)
build_graph(data)
# islands = {'Sample_num': 0, 'Island ID': None, 'Score': 2048}, {'Sample_num': 2, 'Island ID': 3, 'Score': 2048}, {'Sample_num': 2, 'Island ID': 0, 'Score': 2124}, {'Sample_num': 2, 'Island ID': 1, 'Score': 2048}, {'Sample_num': 3, 'Island ID': 1, 'Score': 2048}, {'Sample_num': 3, 'Island ID': 1, 'Score': 2048}, {'Sample_num': 3, 'Island ID': 1, 'Score': 2426}, {'Sample_num': 3, 'Island ID': 3, 'Score': 2048}, {'Sample_num': 3, 'Island ID': 0, 'Score': 2048}, {'Sample_num': 4, 'Island ID': 1, 'Score': 2048}, {'Sample_num': 5, 'Island ID': 1, 'Score': 2048}, {'Sample_num': 4, 'Island ID': 1, 'Score': 2048}, {'Sample_num': 0, 'Island ID': None, 'Score': 2048}, {'Sample_num': 3, 'Island ID': 4, 'Score': 2048}, {'Sample_num': 2, 'Island ID': 4, 'Score': 2048}, {'Sample_num': 3, 'Island ID': 4, 'Score': 2048}, {'Sample_num': 2, 'Island ID': 2, 'Score': 2048}, {'Sample_num': 3, 'Island ID': 2, 'Score': 2048}, {'Sample_num': 2, 'Island ID': 1, 'Score': 2049}, {'Sample_num': 3, 'Island ID': 1, 'Score': 2467}, {'Sample_num': 2, 'Island ID': 3, 'Score': 2048}, {'Sample_num': 2, 'Island ID': 2, 'Score': 2048}, {'Sample_num': 4, 'Island ID': 0, 'Score': 2048}, {'Sample_num': 5, 'Island ID': 3, 'Score': 2224}, {'Sample_num': 5, 'Island ID': 1, 'Score': 2048}, {'Sample_num': 4, 'Island ID': 2, 'Score': 2048}, {'Sample_num': 5, 'Island ID': 2, 'Score': 2048}, {'Sample_num': 5, 'Island ID': 3, 'Score': 2222}, {'Sample_num': 4, 'Island ID': 2, 'Score': 2048}, {'Sample_num': 5, 'Island ID': 4, 'Score': 2048}, {'Sample_num': 4, 'Island ID': 1, 'Score': 2241}, {'Sample_num': 4, 'Island ID': 4, 'Score': 2048}, {'Sample_num': 4, 'Island ID': 0, 'Score': 2048}, {'Sample_num': 5, 'Island ID': 0, 'Score': 2048}, {'Sample_num': 5, 'Island ID': 0, 'Score': 2048}, {'Sample_num': 6, 'Island ID': 3, 'Score': 2220}, {'Sample_num': 7, 'Island ID': 3, 'Score': 2048}, {'Sample_num': 6, 'Island ID': 2, 'Score': 2048}, {'Sample_num': 6, 'Island ID': 3, 'Score': 1644}, {'Sample_num': 7, 'Island ID': 0, 'Score': 2048}, {'Sample_num': 7, 'Island ID': 0, 'Score': 2354}, {'Sample_num': 6, 'Island ID': 2, 'Score': 2048}, {'Sample_num': 7, 'Island ID': 2, 'Score': 2048}, {'Sample_num': 7, 'Island ID': 0, 'Score': 2354}, {'Sample_num': 7, 'Island ID': 4, 'Score': 2048}, {'Sample_num': 6, 'Island ID': 4, 'Score': 2048}, {'Sample_num': 6, 'Island ID': 2, 'Score': 2048}, {'Sample_num': 8, 'Island ID': 2, 'Score': 2077}, {'Sample_num': 9, 'Island ID': 2, 'Score': 2048}, {'Sample_num': 9, 'Island ID': 1, 'Score': 2584}, {'Sample_num': 9, 'Island ID': 2, 'Score': 2371}, {'Sample_num': 8, 'Island ID': 0, 'Score': 2353}, {'Sample_num': 9, 'Island ID': 0, 'Score': 2048}, {'Sample_num': 8, 'Island ID': 2, 'Score': 2323}, {'Sample_num': 9, 'Island ID': 4, 'Score': 2048}, {'Sample_num': 9, 'Island ID': 4, 'Score': 2146}, {'Sample_num': 9, 'Island ID': 4, 'Score': 2048}, {'Sample_num': 8, 'Island ID': 4, 'Score': 2048}, {'Sample_num': 8, 'Island ID': 0, 'Score': 2411}, {'Sample_num': 9, 'Island ID': 0, 'Score': 2411}, {'Sample_num': 8, 'Island ID': 1, 'Score': 2048}, {'Sample_num': 10, 'Island ID': 1, 'Score': 2268}, {'Sample_num': 11, 'Island ID': 1, 'Score': 2096}, {'Sample_num': 10, 'Island ID': 0, 'Score': 2473}, {'Sample_num': 10, 'Island ID': 2, 'Score': 2359}, {'Sample_num': 11, 'Island ID': 4, 'Score': 2048}, {'Sample_num': 11, 'Island ID': 4, 'Score': 2048}, {'Sample_num': 12, 'Island ID': 4, 'Score': 2937}, {'Sample_num': 13, 'Island ID': 0, 'Score': 2048}, {'Sample_num': 13, 'Island ID': 4, 'Score': 2048}, {'Sample_num': 12, 'Island ID': 0, 'Score': 2048}, {'Sample_num': 13, 'Island ID': 0, 'Score': 2473}, {'Sample_num': 12, 'Island ID': 4, 'Score': 2937}, {'Sample_num': 12, 'Island ID': 3, 'Score': 2048}, {'Sample_num': 13, 'Island ID': 3, 'Score': 2215}, {'Sample_num': 13, 'Island ID': 2, 'Score': 2348}, {'Sample_num': 13, 'Island ID': 4, 'Score': 2905}, {'Sample_num': 15, 'Island ID': 2, 'Score': 2113}, {'Sample_num': 14, 'Island ID': 1, 'Score': 2584}, {'Sample_num': 15, 'Island ID': 1, 'Score': 2048}, {'Sample_num': 14, 'Island ID': 1, 'Score': 2048}, {'Sample_num': 15, 'Island ID': 1, 'Score': 2603}, {'Sample_num': 14, 'Island ID': 4, 'Score': 2927}, {'Sample_num': 14, 'Island ID': 2, 'Score': 2386}, {'Sample_num': 14, 'Island ID': 0, 'Score': 2474}, {'Sample_num': 14, 'Island ID': 0, 'Score': 2471}, {'Sample_num': 14, 'Island ID': 1, 'Score': 2603}, {'Sample_num': 15, 'Island ID': 1, 'Score': 2238}, {'Sample_num': 15, 'Island ID': 2, 'Score': 1913}, {'Sample_num': 14, 'Island ID': 3, 'Score': 2220}, {'Sample_num': 15, 'Island ID': 3, 'Score': 2176}, {'Sample_num': 14, 'Island ID': 1, 'Score': 2048}, {'Sample_num': 16, 'Island ID': 1, 'Score': 2048}, {'Sample_num': 16, 'Island ID': 0, 'Score': 2498}, {'Sample_num': 17, 'Island ID': 1, 'Score': 2048}, {'Sample_num': 17, 'Island ID': 1, 'Score': 2048}, {'Sample_num': 16, 'Island ID': 1, 'Score': 2048}, {'Sample_num': 16, 'Island ID': 4, 'Score': 2171}, {'Sample_num': 17, 'Island ID': 4, 'Score': 2441}, {'Sample_num': 16, 'Island ID': 3, 'Score': 2048}, {'Sample_num': 17, 'Island ID': 3, 'Score': 2210}, {'Sample_num': 16, 'Island ID': 4, 'Score': 2410}, {'Sample_num': 16, 'Island ID': 1, 'Score': 2167}, {'Sample_num': 19, 'Island ID': 3, 'Score': 2048}, {'Sample_num': 19, 'Island ID': 3, 'Score': 2215}, {'Sample_num': 19, 'Island ID': 4, 'Score': 2929}, {'Sample_num': 18, 'Island ID': 3, 'Score': 2216}, {'Sample_num': 18, 'Island ID': 0, 'Score': 2498}, {'Sample_num': 19, 'Island ID': 0, 'Score': 2467}, {'Sample_num': 18, 'Island ID': 1, 'Score': 2603}, {'Sample_num': 19, 'Island ID': 3, 'Score': 2224}, {'Sample_num': 19, 'Island ID': 0, 'Score': 2048}, {'Sample_num': 20, 'Island ID': 0, 'Score': 2048}, {'Sample_num': 21, 'Island ID': 3, 'Score': 2229}, {'Sample_num': 21, 'Island ID': 1, 'Score': 2048}, {'Sample_num': 21, 'Island ID': 0, 'Score': 2048}, {'Sample_num': 21, 'Island ID': 1, 'Score': 2048}, {'Sample_num': 20, 'Island ID': 2, 'Score': 2316}, {'Sample_num': 20, 'Island ID': 4, 'Score': 2102}, {'Sample_num': 21, 'Island ID': 4, 'Score': 2414}, {'Sample_num': 21, 'Island ID': 3, 'Score': 2048}
# append_to_pickle(new_file_path, islands)

