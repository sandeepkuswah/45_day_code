# cook your dish here
# Number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Read the values of X and Y
    X, Y = map(int, input().split())
    
    # Calculate how much water is needed for one person
    water_needed_per_person = 2 * Y
    
    # Calculate the maximum number of people who can bathe
    max_people = X // water_needed_per_person
    
    # Output the result for the current test case
    print(max_people)
    