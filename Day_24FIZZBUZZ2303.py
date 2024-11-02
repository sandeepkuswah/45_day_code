# cook your dish here
# Read number of test cases
T = int(input())
results = []

for _ in range(T):
    N = int(input())
    # Calculate the number of choices for captain and vice-captain
    choices = N * (N - 1)
    results.append(choices)

# Print all results for the test cases
for result in results:
    print(result)
    