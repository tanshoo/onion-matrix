import timeit
import numpy as np
from OnionMatrix import OnionMatrix

# Sample OnionMatrix and vector
n, m = 1000, 10

v = np.random.rand(m*n)
blocks = [np.random.rand(m,m) for _ in range(n)]
onion_matrix = OnionMatrix(blocks)

def benchmark_multiply():
    onion_matrix.multiply(v)

def benchmark_solve():
    onion_matrix.solve(v)

# Benchmark the methods
num_runs = 5000

execution_time = timeit.timeit(benchmark_multiply, number=num_runs)
print(f"Average execution time over {num_runs} runs: {execution_time / num_runs:.6f} seconds")

execution_time = timeit.timeit(benchmark_solve, number=num_runs)
print(f"Average execution time over {num_runs} runs: {execution_time / num_runs:.6f} seconds")