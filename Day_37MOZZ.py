# cook your dish here
import math

# Function to calculate the maximum number of plates Chef could have ordered
def max_plates(X, Y, R):
    # Calculate the number of extra mozzarella sticks
    extra_sticks = R // 30
    # Total sticks Chef ate
    total_sticks = X + extra_sticks
    # Calculate the number of plates (rounding up)
    plates = math.ceil(total_sticks / Y)
    return plates

# Main function to handle input and output
def main():
    # Read number of test cases
    T = int(input())
    
    # Process each test case
    for _ in range(T):
        # Read X, Y, R for each test case
        X, Y, R = map(int, input().split())
        # Calculate and print the result for this test case
        print(max_plates(X, Y, R))

# Run the main function
if __name__ == "__main__":
    main()
    