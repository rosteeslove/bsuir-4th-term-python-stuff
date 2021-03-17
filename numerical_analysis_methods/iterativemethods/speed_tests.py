"""
This module contains a script to compare time comlexity
of iterative methods and Gaussian elimination method variations.
"""


# pylint: disable=import-error


import time
import os,sys,inspect
import numpy as np
import matplotlib.pyplot as plt

import base_method as bm
import simple_iterations_method as sim
import seidel_method as sm
import examples

# I hope the following code is ok:
current_dir = os.path.dirname(os.path.abspath(
              inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
from gaussianelimination import gauss_elim_no_pivoting_as_it_is as genp
from gaussianelimination import gauss_elim_partial_pivoting as gepp
from gaussianelimination import gauss_elim_complete_pivoting as gecp


eps = 0.000001

g1_times = []
g2_times = []
g3_times = []

sim_times = []
sm_times = []

np_times = []

for size in range(16, 256):
    b = np.random.rand(size)
    while True:
        A = (size * np.identity(size) + np.random.rand(size, size))
        if bm.check_convergence(A, b):
            break

    time1 = time.time()
    gauss1_sol = genp.solve(A, b, False)
    time2 = time.time()
    g1_times.append(time2-time1)

    time1 = time.time()
    gauss2_sol = gepp.solve(A, b, False)
    time2 = time.time()
    g2_times.append(time2-time1)

    time1 = time.time()
    gauss3_sol = gecp.solve(A, b, False)
    time2 = time.time()
    g3_times.append(time2-time1)

    time1 = time.time()
    sim_sol = sim.solve(A, b, eps)
    time2 = time.time()
    sim_times.append(time2-time1)

    time1 = time.time()
    sm_sol = sm.solve(A, b, eps)
    time2 = time.time()
    sm_times.append(time2-time1)

    time1 = time.time()
    np_sol = np.linalg.solve(A, b)
    time2 = time.time()
    np_times.append(time2-time1)

    true_sol = np.linalg.solve(A, b)
    gauss1_error = np.absolute(true_sol) - np.absolute(gauss1_sol)
    gauss2_error = np.absolute(true_sol) - np.absolute(gauss2_sol)
    gauss3_error = np.absolute(true_sol) - np.absolute(gauss3_sol)
    sim_error = np.absolute(true_sol) - np.absolute(sim_sol[0])
    sm_error = np.absolute(true_sol) - np.absolute(sm_sol[0])

    print('MATRIX SIZE = {0}'.format(size))
    print(true_sol)
    print('the biggest error for Gaussian method '
          'w/o pivoting is: {0}'.format(np.amax(gauss1_error)))
    print('the biggest error for Gaussian method '
          'w/ partial pivoting is: {0}'.format(np.amax(gauss2_error)))
    print('the biggest error for Gaussian method '
          'w/ complete pivoting is: {0}'.format(np.amax(gauss3_error)))
    print('the biggest error for sim: {0}\n{1} iterations.'.format(np.amax(sim_error), sim_sol[1]))
    print('the biggest error for '
          ' Seidel method: {0}\n{1} iterations.\n\n\n'.format(np.amax(sm_error), sm_sol[1]))

#plt.plot(g1_times, label='Gauss w/o pivoting')
#plt.plot(g2_times, label='Gauss w/ partial pivoting')
#plt.plot(g3_times, label='Gauss w/ complete pivoting')
plt.plot(sim_times, label='simple iterations')
plt.plot(sm_times, label='Seidel')
plt.plot(np_times, label='numpy linalg solve')
plt.legend()
plt.show()


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