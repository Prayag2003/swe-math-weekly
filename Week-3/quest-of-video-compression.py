import numpy as np

def solve_compression_contributions():
    N, M = map(int, input().split())
    A = []  
    b = [] 
    
    for _ in range(M):
        data = list(map(int, input().split()))
        A.append(data[:-1])  
        b.append(data[-1])  
    
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    
    try:
        # solve linear system Ax = b
        x = np.linalg.solve(A, b)
        
        # invalid solution 
        if not np.allclose(A @ x, b, atol=1e-6):
            print("observation error")
        else:
            print(" ".join(f"{val:.8f}" for val in x))
    except np.linalg.LinAlgError:
        print("observation error")

solve_compression_contributions()
