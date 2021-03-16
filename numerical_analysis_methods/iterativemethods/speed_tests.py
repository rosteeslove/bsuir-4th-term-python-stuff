"""
This module is to contain a few methods to compare time comlexity
of iterative methods and Gaussian elimination method variations.
"""


# pylint: disable=import-error


import os,sys,inspect
import numpy as np
import matplotlib.pyplot as plt

import simple_iterations_method as sim
import seidel_method as sm
import examples

# I hope the following code is ok:
current_dir = os.path.dirname(os.path.abspath(
              inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
import gaussianelimination


"""
This code is here bc I don't know where else could it be.

To understand the relations between sim-converging
matrix set and seidel-converging matrix-set:

while True:
    R = 100*(2*np.random.rand(3, 3) - 1)
    r = 100*(2*np.random.rand(3) - 1)

    if bm.check_convergence(R, r):
        continue

    try:
        x1 = np.linalg.solve(R, r)
    except:
        continue

    x2 = sim.solve(R, r, 0.001)[0]
    x3 = sm.solve(R, r, 0.001)[0]

    sim_error = np.absolute(x1 - x2)
    sm_error = np.absolute(x1 - x3)

    if (sim_error < 0.001).all() and not (sm_error < 0.001).all():
        print(R)
        print(r)
        break
"""