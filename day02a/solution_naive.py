import pathlib

script_dir = pathlib.Path(__file__).parent
input_file = script_dir / "input.txt"

safe_reports = 0

with open(input_file, "r") as f:
    for line in f:
        report = [float(val) for val in line.split()]
        diff = [x - report[i - 1] for i, x in enumerate(report) if i > 0]

        abs_diff = [abs(val) for val in diff]
        if abs(sum(diff)) != sum(abs_diff):
            continue

        diff = abs_diff

        max_diff = max(diff)
        if max_diff > 3:
            continue

        min_diff = min(diff)
        if min_diff == 0:
            continue

        safe_reports += 1

print(f"Safe Reports: {safe_reports}")
