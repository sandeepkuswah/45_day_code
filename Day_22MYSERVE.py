# cook your dish here
def determine_serves(T, test_cases):
    results = []
    for case in test_cases:
        P, Q = case
        total_points = P + Q
        total_serves = total_points + 1  # Include initial serve
        if (total_serves // 2) % 2 == 0:
            results.append("Alice")
        else:
            results.append("Bob")
    return results

# Input reading
T = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(T)]

# Get results
results = determine_serves(T, test_cases)

# Output results
for result in results:
    print(result)
    