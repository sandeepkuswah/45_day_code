# cook your dish here
# Read number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Read the times for bike and car
    X, Y = map(int, input().split())
    
    # Compare the times and print the result
    if X < Y:
        print("BIKE")
    elif X > Y:
        print("CAR")
    else:
        print("SAME")
        