from pydrake.all import MathematicalProgram, Solve
import pypolycontain as pp
import numpy as np

def is_contained_in(A_x, b_x, A_y, b_y, n_dim_proj: int) -> bool:
    prog = MathematicalProgram()

    X = pp.H_polytope(A_x, b_x)
    Y = pp.H_polytope(A_y, b_y)

    T_x = np.hstack((np.zeros((n_dim_proj, A_x.shape[1] - n_dim_proj)),np.eye(n_dim_proj)))
    T_y = np.hstack((np.zeros((n_dim_proj, A_y.shape[1] - n_dim_proj)),np.eye(n_dim_proj)))

    AH_X = pp.AH_polytope(np.zeros((n_dim_proj,1)), T_x, X)
    AH_Y = pp.AH_polytope(np.zeros((n_dim_proj,1)), T_y, Y)
    # https://github.com/sadraddini/pypolycontain/blob/master/pypolycontain/containment.py
    # -1 for sufficient condition
    # pick `0` for necessary and sufficient encoding (may be too slow) (2019b)
    pp.subset(prog, AH_X, AH_Y, -1)
    result = Solve(prog)
    return result.is_success()


A_x=np.array([[1,1],[-1,1],[0,-1]])
b_x=np.array([1,1,0])
A_y=np.array([[1,1],[-1,1],[0,-1]])
b_y=np.array([1,1,0])

print(is_contained_in(A_x, b_x, A_y, b_y, 1)) # True