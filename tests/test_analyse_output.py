import re


def average(items):
    return sum(items) / len(items)


def test_compute_average_duration():
    with open("output_duration.txt") as f:
        lines = f.readlines()
    
    durations = []
    for line in lines:
        match = re.search(r"succeeded in ([\d\.]+)s", line)
        if match:
            durations.append(float(match.group(1)))
    
    print(f"Average duration: {average(durations)}")
        