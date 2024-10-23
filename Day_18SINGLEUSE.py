# cook your dish here
import math

def min_attacks_to_win(T, test_cases):
    results = []
    for i in range(T):
        H, X, Y = test_cases[i]
        
        # Calculate normal attacks only
        normal_attacks_only = math.ceil(H / X)
        
        # Calculate attacks after using special attack
        remaining_health_after_special = H - Y
        if remaining_health_after_special > 0:
            normal_attacks_after_special = math.ceil(remaining_health_after_special / X)
            total_attacks_with_special = 1 + normal_attacks_after_special
        else:
            total_attacks_with_special = 1  # Special attack wins immediately

        # Minimum attacks needed
        min_attacks = min(normal_attacks_only, total_attacks_with_special)
        results.append(min_attacks)
    
    return results

# Sample Input
T = 4
test_cases = [
    (100, 25, 40),
    (100, 29, 45),
    (46, 1, 2),
    (78, 15, 78)
]

# Get results
results = min_attacks_to_win(T, test_cases)
for result in results:
    print(result)
    