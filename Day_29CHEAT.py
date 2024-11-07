# cook your dish here
def count_tuesdays(N):
    if N < 2:
        return 0
    return (N - 2) // 7 + 1

# Reading number of test cases
T = int(input())

# Processing each test case
for _ in range(T):
    N = int(input())
    print(count_tuesdays(N))
    