"""
This script exists for the following reasons:

- to compare simple iterations method (sim) and Seidel method (sm)
  i.e. to compare number of iterations both require for the
  result within epsilon error.

- to explore the relation between 2 sets
  of systems of linear equations:
  - systems for which the correct answer can be found by sim.
  - systems for which the correct answer can be found by sm.
"""


import time
import numpy as np

import base_method as bm
import simple_iterations_method as sim
import seidel_method as sm
import examples


def solve(A, b, eps):
    """
    Print the results of simple iteration method, Seidel method
    and numpy.linalg.solve method.
    """
    print('The matrix is:\n{0}\n\nThe vector is:\n{1}\n\n'.format(A, b))

    try:
        x = sim.solve(A, b, eps)
        print('The result of simple iteration method is:\n{0}\n\n'.format(x))
    except Exception:
        print('Simple iteration method failed.\n\n')

    try:
        x = sm.solve(A, b, eps)
        print('The result of Seidel method is:\n{0}\n\n'.format(x))
    except Exception:
        print('Seidel method failed.\n\n')

    try:
        x = np.linalg.solve(A, b)
        print('The result of np.linalg.solve is:\n{0}\n\n'.format(x))
    except Exception:
        print('np.linalg.solve failed.\n\n')


def main():
    print('A simple matrix:\n')
    solve(examples.A, examples.b, 0.0001)

    print('\n\n\nA strictly diagonally dominant matrix:\n')
    solve(examples.E, examples.e, 0.0001)
    
    print('\n\n\nAn unsolvable-system matrix:\n')
    solve(examples.F, examples.f, 0.0001)

    print('\n\n\nA matrix that does not meet the convergence criteria '
          'that does not converge:\n')
    solve(examples.G, examples.g, 0.0001)

    print('\n\n\nA matrix that does not meet the convergence criteria '
          'that does converge when simple iteration method is run:\n')
    solve(examples.H, examples.h, 0.0001)

    print('\n\n\nA matrix that does not meet the convergence criteria '
          'that does converge when Seidel method is run:\n')
    solve(examples.K, examples.k, 0.0001)

    print('\n\n\nA matrix that does not meet the convergence criteria '
          'that does converge when both methods are run:\n')
    solve(examples.M, examples.m, 0.0001)


if __name__ == "__main__":
    main()
