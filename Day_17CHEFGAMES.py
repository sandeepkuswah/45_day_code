# cook your dish here
# Read the number of test cases
T = int(input())

# Loop through each test case
for _ in range(T):
    # Read the decisions of the 4 referees
    decisions = list(map(int, input().split()))
    
    # If all decisions are 0, the ball is IN, otherwise OUT
    if all(d == 0 for d in decisions):
        print("IN")
    else:
        print("OUT")
        