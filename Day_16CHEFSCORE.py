# cook your dish here
# Read number of test cases
T = int(input())

# Loop through each test case
for _ in range(T):
    # Read N (number of problems), X (marks per problem), Y (desired total marks)
    N, X, Y = map(int, input().split())
    
    # Check if Y is a multiple of X and if the number of full-mark problems does not exceed N
    if Y % X == 0 and Y // X <= N:
        print("YES")
    else:
        print("NO")
        