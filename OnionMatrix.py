import numpy as np

class OnionMatrix:
    """
    Class representing an onion matrix
    :param blocks: List of matrices A_1, A_2, ..., A_n
    
    Note:
    This class assumes that the arguments passed to its methods 
    are correct and does not perform any validation.
    """

    blocks: np.ndarray
    n: int 
    m: int 


    def __init__(self, blocks: list[np.ndarray]) -> None:
        self.blocks = np.array(blocks)
        self.n = len(blocks)
        self.m = len(blocks[0])


    def multiply(self, v: np.ndarray) -> np.ndarray:
        """
        Multiply the onion matrix by a vector v of length n*m.
        :param v: Vector of length n*m
        :return: The result of the multiplication
        """

        v_blocks = v.reshape(self.n, self.m)
        diagonal_blocks = np.einsum('ijk,ik->ij', self.blocks, v_blocks)
        prefix_sums = np.cumsum(diagonal_blocks, axis=0)
        suffix_vector_sums = np.cumsum(v_blocks[::-1], axis=0)[::-1]
        suffix_sums = np.einsum('ijk,ik->ij', self.blocks, suffix_vector_sums)
        result_blocks = prefix_sums + suffix_sums - diagonal_blocks

        return result_blocks.ravel()


    def solve(self, b: np.ndarray) -> np.ndarray:
        pass