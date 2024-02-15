from collections import Counter

def solve(s):
    counts = Counter(s)
    values = list(counts.values())
    if len(set(values)) <= 1:  # Check if all counts are already equal
        return True
    for i in range(len(values)):
        if all(abs(values[j] - values[i]) <= 1 for j in range(len(values)) if j != i):
            return True
    return False

# Test case
print(solve('abbccc'))