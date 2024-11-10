# cook your dish here
def is_cyclic_quadrilateral(A, B, C, D):
    # Check if opposite angles sum to 180
    return (A + C == 180) and (B + D == 180)

# Read the number of test cases
T = int(input())

for _ in range(T):
    # Read the angles for the current test case
    A, B, C, D = map(int, input().split())
    
    # Check if the quadrilateral is cyclic
    if is_cyclic_quadrilateral(A, B, C, D):
        print("YES")
    else:
        print("NO")
        