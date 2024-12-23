import numpy as np

class OnionMatrix:
    """
    Class representing an onion matrix
    :param blocks: List of matrices A_1, A_2, ..., A_n
    
    Note:
    This class assumes that the arguments passed to its methods 
    are correct and does not perform any validation.
    """

    blocks: list[np.ndarray]
    n: int 
    m: int 


    def __init__(self, blocks: list[np.ndarray]) -> None:
        self.blocks = blocks
        self.n = len(blocks)
        self.m = len(blocks[0])


    def multiply(self, v: np.ndarray) -> np.ndarray:
        """
        Multiply the onion matrix by a vector v of length n*m.
        :param v: Vector of length n*m
        :return: The result of the multiplication
        """

        prefix_sum = np.zeros(self.m)
        suffix_vector_sum = np.sum(
            v[i*self.m : (i+1)*self.m] for i in range(self.n)
        )
        result = np.empty_like(v)

        for i in range(self.n):
            v_block = v[i*self.m : (i+1)*self.m]
            prefix_sum += self.blocks[i] @ v_block
            suffix_vector_sum -= v_block
            result[i*self.m : (i+1)*self.m] = prefix_sum + self.blocks[i] @ suffix_vector_sum

        return result


    def solve(self, b: np.ndarray) -> np.ndarray:
        pass