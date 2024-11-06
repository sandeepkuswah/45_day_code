# cook your dish here
# Read number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Read the values X, A, B for each test case
    X, A, B = map(int, input().split())
    
    # Calculate the total score
    total_score = A * 1 + B * 2
    
    # Check if Chef qualifies
    if total_score >= X:
        print("Qualify")
    else:
        print("NotQualify")
        