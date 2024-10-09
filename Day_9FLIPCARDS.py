# cook your dish here
# Input number of test cases
T = int(input())

# Loop through all test cases
for _ in range(T):
    # Input the total number of cards (N) and the number of face-up cards (X)
    N, X = map(int, input().split())
    
    # Calculate the minimum number of flips needed
    flips = min(X, N - X)
    
    # Output the result for this test case
    print(flips)
    