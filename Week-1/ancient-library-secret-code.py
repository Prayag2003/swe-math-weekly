from typing import List
import numpy as np

def can_unlock_library(keys: List[List[float]], tolerance: float = 1e-10) -> bool:

    matrix = np.array(keys, dtype=float)

    n = len(matrix)
    if n != len(matrix[0]):
        return False

    # gaussian elimination to check for linear independence
    rank = np.linalg.matrix_rank(matrix, tol=tolerance)

    # if rank == dimension, the keys form a basis
    return rank == n

def main():
    keys1 = [
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0],
        [0.0, 0.0, 1.0]
    ]
    keys2 = [
        [2, 0, 0],
        [0, 2, 0],
        [4, 4, 0]
    ]
    
    print(can_unlock_library(keys1))  
    print(can_unlock_library(keys2))  

main()