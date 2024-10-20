# cook your dish here
import math

# Function to calculate the total time for the event
def total_event_time(N, A, B):
    rounds = int(math.log2(N))  # Number of rounds is log2(N)
    total_round_time = rounds * A
    total_break_time = (rounds - 1) * B
    return total_round_time + total_break_time

# Reading the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    N, A, B = map(int, input().split())
    # Calculate the total time for this test case
    result = total_event_time(N, A, B)
    print(result)
    