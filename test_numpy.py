import numpy as np

print(f"NumPy version: {np.__version__}")

# Your original scenario
x = np.array([6., 0., 0., 0., 0., 0., 0., 0., 0., 0.])
print("Initial x:", x)
i = np.array([2, 3, 3, 4, 4, 4])
print("Index i:", i)
x[i] += 1
print("Result of x[i] += 1:", x)

print("\n--- Minimal Test ---")
# Simple accumulation test
test_x = np.zeros(5)
test_i = np.array([1, 1, 1])
print("Initial test_x:", test_x)
test_x[test_i] += 1
print("Result of test_x[test_i] += 1:", test_x)