"""
TODO: compare time complexity of gauss and seidel.
"""

import numpy as np

"""
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