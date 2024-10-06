# cook your dish here
def cooler_dilemma(test_cases):
    results = []
    for X, Y in test_cases:
        if X >= Y:
            results.append(0)
        else:
            M = (Y // X) - 1
            results.append(M)
    return results

# Input lena
T = int(input().strip())
test_cases = []
for _ in range(T):
    X, Y = map(int, input().strip().split())
    test_cases.append((X, Y))

# Results nikaalna
results = cooler_dilemma(test_cases)

# Results output karna
for result in results:
    print(result)
