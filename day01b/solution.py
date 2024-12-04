import numpy as np
import pathlib

script_dir = pathlib.Path(__file__).parent.parent
input_file = script_dir / "day01a" / "input.txt"

ids = np.loadtxt(input_file, dtype=np.uint32)

unique_0, count_0 = np.unique_counts(ids[:, 0])
unique_1, count_1 = np.unique_counts(ids[:, 1])
common_values, index_0, index_1 = np.intersect1d(
    unique_0, unique_1, return_indices=True
)

result = np.sum(common_values * count_0[index_0] * count_1[index_1])

print(f"Similarity Score: {result}")
