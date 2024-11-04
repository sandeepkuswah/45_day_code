# cook your dish here
# Read number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    N = int(input())
    # Check if N is a multiple of 4
    if N % 4 == 0:
        print("Good")
    else:
        print("Not Good")
        