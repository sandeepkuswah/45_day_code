# cook your dish here
def min_steps_to_reach(T, test_cases):
    results = []
    for i in range(T):
        A, B, K = test_cases[i]
        distance = abs(A - B)
        if distance == 0:
            results.append(0)
        else:
            steps = (distance + K - 1) // K
            results.append(steps)
    return results

# Reading input
T = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(T)]

# Getting results
results = min_steps_to_reach(T, test_cases)

# Printing results
for result in results:
    print(result)
