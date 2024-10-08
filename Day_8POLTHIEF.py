# cook your dish here
# Input number of test cases
T = int(input())

# Loop through all test cases
for _ in range(T):
    # Input the positions of the policeman (X) and the thief (Y)
    X, Y = map(int, input().split())
    
    # Calculate the minimum time to catch the thief
    # It's the absolute difference between their positions
    time_taken = abs(X - Y)
    
    # Output the result
    print(time_taken)
    