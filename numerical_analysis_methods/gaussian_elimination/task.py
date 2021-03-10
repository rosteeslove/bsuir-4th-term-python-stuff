import numpy as np

import gauss_elim_no_pivoting as genp
import gauss_elim_no_pivoting_as_it_is as genpaii
import gauss_elim_partial_pivoting as gepp
import gauss_elim_complete_pivoting as gecp

import tests



"""
The task is to compare the variations of Gaussian elimination method
of solving systems of linear equations.
"""



interactive = False

def solve(A, b):
    try:
        x1 = genpaii.solve(A, b, interactive)
        print('Результат решения по схеме единственного деления:\n{0}\n'.format(x1))
    except:
        print('Схема единственного деления не дала результата\n')


    try:
        x2 = gepp.solve(A, b, interactive)
        print('Результат решения по схеме частичного выбора:\n{0}\n'.format(x2))
    except:
        print('Схема частичного выбора не дала результата\n')


    try:
        x3 = gecp.solve(A, b, interactive)
        print('Результат решения по схеме полного выбора:\n{0}\n'.format(x3))
    except:
        print('Схема полного выбора не дала результата\n')

    
    try:
        x4 = np.linalg.solve(A, b)
        print('Результат решения средствами numpy:\n{0}\n'.format(x4))
    except:
        print('Средства numpy не дали результата\n')
    


def main():

    print('Система из задания:\n')
    print('A = {0}\n'.format(tests.A))
    print('b = {0}\n\n'.format(tests.b))

    solve(tests.A, tests.b)
    print('\n\n---------------------------\n\n')
    solve(tests.T1, tests.v1)
    print('\n\n---------------------------\n\n')
    solve(tests.T2, tests.v2)
    print('\n\n---------------------------\n\n')
    solve(tests.T3, tests.v3)
    print('\n\n---------------------------\n\n')
    solve(tests.T4, tests.v4)
    print('\n\n---------------------------\n\n')
    solve(tests.T5, tests.v5)
    


if __name__ == "__main__":
    main()

