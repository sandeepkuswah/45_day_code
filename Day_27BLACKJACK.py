# cook your dish here
# Read the number of test cases
T = int(input())

# Loop through each test case
for _ in range(T):
    # Read the two numbers A and B
    A, B = map(int, input().split())
    
    # Calculate the third number needed to make the sum 21
    C = 21 - (A + B)
    
    # Check if C is a valid number between 1 and 10
    if 1 <= C <= 10:
        print(C)
    else:
        print(-1)
        