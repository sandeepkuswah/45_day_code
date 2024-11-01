# cook your dish here
def is_score_possible(test_cases):
    results = []
    for A, B, C, D in test_cases:
        if C >= A and D >= B:
            results.append("POSSIBLE")
        else:
            results.append("IMPOSSIBLE")
    return results

# Input reading
T = int(input())
test_cases = []
for _ in range(T):
    A, B = map(int, input().split())
    C, D = map(int, input().split())
    test_cases.append((A, B, C, D))

# Process and output results
results = is_score_possible(test_cases)
for result in results:
    print(result)
    