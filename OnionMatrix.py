import numpy as numpy

class OnionMatrix:
    """
    Class representing an onion matrix
    :param blocks: List of matrices A_1, A_2, ..., A_n
    """

    blocks: list[np.ndarray]
    n: int 
    m: int 


    def __init__(self, blocks: list[np.ndarray]) -> None:
        self.blocks = blocks
        self.n = len(blocks)
        self.m = len(blocks[0])
