# cook your dish here
# Function to check if exact weight can be measured
def can_measure_exact_weight(W, X, Y, Z):
    # Check all possible combinations
    if W == X or W == Y or W == Z or W == X + Y or W == X + Z or W == Y + Z or W == X + Y + Z:
        return "YES"
    else:
        return "NO"

# Read number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Read W, X, Y, Z values
    W, X, Y, Z = map(int, input().split())
    
    # Output whether it's possible to measure the exact weight
    print(can_measure_exact_weight(W, X, Y, Z))
    