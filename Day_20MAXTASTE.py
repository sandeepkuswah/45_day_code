# cook your dish here
def max_tastiness(test_cases):
    results = []
    for case in test_cases:
        a, b, c, d = case
        # Calculate tastiness for all combinations
        tastiness_1 = a + c
        tastiness_2 = a + d
        tastiness_3 = b + c
        tastiness_4 = b + d
        
        # Find the maximum tastiness
        max_tastiness = max(tastiness_1, tastiness_2, tastiness_3, tastiness_4)
        results.append(max_tastiness)
    return results

# Read input
T = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(T)]

# Calculate and print results
results = max_tastiness(test_cases)
for result in results:
    print(result)
    