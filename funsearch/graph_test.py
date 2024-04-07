import numpy as np
import matplotlib.pyplot as plt

data = [
    {'Sample_num': 0, 'Island ID': None, 'Input': 11, 'Score': 2048},
    {'Sample_num': 1, 'Island ID': 4, 'Input': 11, 'Score': 2588},
    {'Sample_num': 1, 'Island ID': 2, 'Input': 11, 'Score': 2048},
    {'Sample_num': 1, 'Island ID': 0, 'Input': 11, 'Score': 2048},
    {'Sample_num': 1, 'Island ID': 0, 'Input': 11, 'Score': 2312},
    {'Sample_num': 1, 'Island ID': 0, 'Input': 11, 'Score': 2048}
]

# Initialize matrix to store scores for each island ID
max_samples = max(d['Sample_num'] for d in data) + 1
num_islands = max(d['Island ID'] for d in data if d['Island ID'] is not None) + 1
score_matrix = np.zeros((num_islands, max_samples))

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