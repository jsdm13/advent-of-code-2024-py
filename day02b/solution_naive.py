import pathlib
import numpy as np

script_dir = pathlib.Path(__file__).parent.parent

input_file = script_dir / "day02a" / "input.txt"

safe_reports = 0
retry_reports = []
line_id = -1


def is_safe(report: np.ndarray) -> bool:
    has_equal_elem = report[:-1] == report[1:]
    equal_score = np.sum(has_equal_elem)

    if equal_score >= 1:
        return False

    above_max_diff = np.abs(report[:-1] - report[1:]) > 3
    above_max_diff_score = np.sum(above_max_diff)

    if above_max_diff_score >= 1:
        return False

    # Test if array is sorted increasing
    # Compares all but last value to all but first value
    # (i.e sorted comparison)
    is_sorted = report[:-1] > report[1:]

    if np.sum(is_sorted) >= np.shape(is_sorted)[0] - 1:
        is_sorted = np.logical_not(is_sorted)

    sort_score = np.sum(is_sorted)

    if sort_score >= 1:
        return False

    # All tests pass, the report is valid
    return True


with open(input_file, "r") as f:
    for line in f:
        line_id += 1
        report = np.asarray([float(val) for val in line.split()])

        if is_safe(report):
            safe_reports += 1
            continue

        for i in range(len(report)):
            if is_safe(np.delete(report, i)):
                safe_reports += 1
                break


print(f"Safe Reports: {safe_reports}")
