# cook your dish here
# Read number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Read values for N (number of episodes), A (even-indexed duration), and B (odd-indexed duration)
    N, A, B = map(int, input().split())
    
    # Calculate the number of odd and even indexed episodes
    odd_count = (N + 1) // 2  # Number of odd-indexed episodes (1, 3, 5, ...)
    even_count = N // 2       # Number of even-indexed episodes (2, 4, 6, ...)
    
    # Calculate total duration
    total_duration = odd_count * B + even_count * A
    
    # Print the total duration for the current test case
    print(total_duration)
    