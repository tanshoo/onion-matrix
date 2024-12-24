# 🧅 Onion Matrix 🧅

This project implements an OnionMatrix class (a special type of matrix) with efficient operations for:
- Multiplication by a vector
- Solving systems of linear equations

All operations are optimized and vectorized using NumPy to ensure fast performance.

The project also includes benchmarking and testing scripts to evaluate the performance and correctness of the implemented methods. It was created as part of the Numerical Methods course at MIM UW.

[Full task description (in Polish)](proj2_opis.pdf)

## Onion Matrix Definition
Let  $n, m \in \mathbb{N}$. A matrix $A$ of dimensions $nm \times nm$ is called an Onion Matrix if it has the following form:

$$
A =
\begin{bmatrix}
A_1 & A_1 & A_1 & \dots & A_1 & A_1 \\
A_1 & A_2 & A_2 & \dots & A_2 & A_2 \\
A_1 & A_2 & A_3 & \dots & A_3 & A_3 \\
\vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\
A_1 & A_2 & A_3 & \dots & A_{n-1} & A_{n-1} \\
A_1 & A_2 & A_3 & \dots & A_{n-1} & A_n
\end{bmatrix}
$$

Each $A_i$ $(1 \leq i \leq n )$ is a square matrix of dimensions $m \times m$. Specifically, the submatrix of $A$ formed by rows $(k-1)m + 1 \dots km$ and columns $(l-1)m + 1 \dots  lm$ $( 1 \leq k, l \leq n )$ equals $A_{\min(k, l)}$.

## Installation
1. Clone the repository
```sh
git clone https://github.com/tanshoo/onion-matrix.git
cd onion-matrix
```

2. Install required dependencies
```sh
pip install numpy
```

## Methods
` __init__(self, blocks: list[np.ndarray]) -> None`

Constructs the onion matrix with the given `blocks`
- Time complexity: $O(nm^2)$

`multiply(self, v: np.ndarray) -> np.ndarray`

Multiplies the onion matrix by a vector `v` and returns the resulting vector
- Time complexity: $O(nm^2)$

`solve(self, b: np.ndarray) -> np.ndarray`

Solves the system of equations (`Ax = b`) and returns the solution vector `x`.
- Time complexity: $O(nm^3)$


## Usage

### OnionMatrix Class

```py
from OnionMatrix import OnionMatrix
import numpy as np

blocks = [np.random.rand(5, 5) for _ in range(10)]

# initialization
onion_matrix = OnionMatrix(blocks)

b = np.random.rand(50)

# solving linear systems
solution = onion_matrix.solve(b)

# multiplication by a vector
assert np.allclose(onion_matrix.multiply(solution), b)
```

### Testing
To check correctness and performance (measured as the slowest run from all):
```sh
python proj2_ocena.py
```

### Benchmarking
To benchmark the `OnionMatrix` methods (measured as the average over all runs):
```sh
python benchmark.py
```