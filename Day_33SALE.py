# Reading the number of test cases
T = int(input())

# Iterate over each test case
for _ in range(T):
    # Read the prices of the three items
    A, B, C = map(int, input().split())
    
    # Calculate the total cost to be paid (sum of two highest prices)
    total_cost = A + B + C - min(A, B, C)
    
    # Output the result for this test case
    print(total_cost)
    
