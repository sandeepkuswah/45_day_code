# cook your dish here
def min_coins_for_gifts(N):
    # Calculate total coins for N gifts
    return 4 * (N // 5) + (N % 5)

def main():
    T = int(input())  # Read the number of test cases
    for _ in range(T):
        N = int(input())  # Read the number of gifts for this test case
        print(min_coins_for_gifts(N))

if __name__ == "__main__":
    main()
    