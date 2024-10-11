# cook your dish here
def max_tastiness(test_cases):
    for case in test_cases:
        a, b, c, d = case
        # Calculate all four possible sums
        max_taste = max(a + c, a + d, b + c, b + d)
        print(max_taste)

# Input
T = int(input())  # Number of test cases
test_cases = [list(map(int, input().split())) for _ in range(T)]

# Output the result for each test case
max_tastiness(test_cases)
