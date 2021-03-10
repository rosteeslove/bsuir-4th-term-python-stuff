import numpy as np

#import jacobi_method as jm

import simple_iterations_method as sim
import seidel_method as sm

k = 14

C = np.array([[0.01, 0., -0.02, 0., 0.],
              [0.01, 0.01, -0.02, 0., 0.],
              [0., 0.01, 0.01, 0., -0.02],
              [0., 0., 0.01, 0.01, 0.],
              [0., 0., 0., 0.01, 0.01]])

D = np.array([[1.33, 0.21, 0.17, 0.12, -0.13],
              [-0.13, -1.33, 0.11, 0.17, 0.12],
              [0.12, -0.13, -1.33, 0.11, 0.17],
              [0.17, 0.12, -0.13, -1.33, 0.11],
              [0.11, 0.67, 0.12, -0.13, -1.33]])

b = np.array([1.2, 2.2, 4.0, 0.0, -1.2])

A = k*C + D

def main(): 
    print(A)
    print(b)
    print(np.linalg.solve(A, b))
    
    x1 = sim.solve(A, b, 0.0001)
    print(x1[0])
    print(x1[1])

    print(A)
    print(b)

    x2 = sm.solve(A, b, 0.0001)
    print(x2[0])
    print(x2[1])


if __name__ == "__main__":
    main()
