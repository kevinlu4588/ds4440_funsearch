import pickle
import numpy as np
import matplotlib.pyplot as plt

def append_to_pickle(file_path, data):
    with open(file_path, 'ab') as f:  # Open file in binary append mode
        pickle.dump(data, f)


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
    max_samples = max(d['Sample_num'] for d in data) + 1
    num_islands = max(d['Island ID'] for d in data if d['Island ID'] is not None) + 1
    score_matrix = np.zeros((num_islands, max_samples)) + 2048

    # Fill the score matrix with scores based on island ID and sample num
    for d in data:
        if d['Island ID'] is not None:
            score_matrix[d['Island ID'], d['Sample_num']] = d['Score']

    # Plotting
    plt.figure(figsize=(10, 6))

    for island_id in range(num_islands):
        plt.plot(range(max_samples), score_matrix[island_id], label=f'Island {island_id}')

    plt.xlabel('Sample Number')
    plt.ylabel('Score')
    plt.title('Scores per Sample Number for Each Island')
    plt.legend()
    plt.grid(True)
    plt.show()

    encountered_pairs = set()

    # Iterate through data and check for duplicates
    for d in data:
        pair = (d['Sample_num'], d['Island ID'])
        if pair in encountered_pairs:
            print(f"Duplicate pair found: {pair}")
        else:
            encountered_pairs.add(pair)

    # If no duplicates found, print message
    if not encountered_pairs:
        print("No duplicate pairs found.")


# Example usage:
# file_path = "scores.pickle"
# data_to_append = {"Island ID": 1, "Score": 0.8}  # Example data to append
# append_to_pickle(file_path, data_to_append)


# Example usage:
file_path = "TurboCap7Iterations.pickle"
data = read_pickle(file_path)
print(data)
build_graph(data)

