# cook your dish here
def find_degree_of_polynomial(test_cases):
    results = []
    
    for _ in range(test_cases):
        N = int(input().strip())  # Number of terms
        coefficients = list(map(int, input().strip().split()))  # Coefficients
        
        # Start from the end to find the highest power with a non-zero coefficient
        degree = -1  # Initialize degree
        for i in range(N - 1, -1, -1):
            if coefficients[i] != 0:
                degree = i  # Update degree
                break
        
        results.append(degree)
    
    return results

# Read number of test cases
T = int(input().strip())
degrees = find_degree_of_polynomial(T)

# Print the results
for degree in degrees:
    print(degree)
    