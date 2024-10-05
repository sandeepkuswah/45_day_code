# cook your dish here
def is_monopoly(test_cases):
    results = []
    for profits in test_cases:
        P, Q, R, S = profits
        total_profit = P + Q + R + S
        
        # Har company ke liye monopoly condition check karna
        if (2 * P > total_profit or 
            2 * Q > total_profit or 
            2 * R > total_profit or 
            2 * S > total_profit):
            results.append("YES")
        else:
            results.append("NO")
    return results

# Input reading
T = int(input())
test_cases = [tuple(map(int, input().split())) for _ in range(T)]

# Monopoly check karke results print karna
results = is_monopoly(test_cases)
for result in results:
    print(result)
