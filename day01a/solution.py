import numpy as np
import pathlib

script_dir = pathlib.Path(__file__).parent
input_file = script_dir / "input.txt"

# use int64 instead of uint64 to avoid underflow in the distances calculation
ids = np.loadtxt(input_file, dtype=np.int64)

# sorts input in place
np.ndarray.sort(ids, axis=0)

distances = np.sum(np.abs(ids[:, 1] - ids[:, 0]))

print(f"Total Distance: {distances}")
