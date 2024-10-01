# cook your dish here
# Input: Four space-separated integers A, B, C, X
A, B, C, X = map(int, input().split())

# Check if X is in the prepared topics A, B, or C
if X in (A, B, C):
    print("Yes")
else:
    print("No")
    