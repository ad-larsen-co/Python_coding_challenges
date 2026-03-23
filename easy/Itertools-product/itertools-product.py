from itertools import product

# Read input
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Compute Cartesian product
result = list(product(A, B))

# Print output
for pair in result:
    print(pair, end=" ")