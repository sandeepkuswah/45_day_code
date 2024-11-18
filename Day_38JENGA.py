# cook your dish here
# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Read N and X for each test case
    N, X = map(int, input().split())
    
    # Check if X is divisible by N
    if X % N == 0:
        print("YES")
    else:
        print("NO")
        