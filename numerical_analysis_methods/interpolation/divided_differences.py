"""
This module facilitates Newton's and Hermite's interpolation
algorithms by providing functions for the calculation of
divided differences.
"""


import math


def setup_newton_table(nodes):
    """
    Return xs list and a divided differences jagged 2d list filled
    with initial values.
    """
    xs = [node[0] for node in nodes]

    node_num = len(nodes)
    table = [[None for _ in range(node_num-i)] for i in range(node_num)]
    for rank, row in enumerate(table):
        row[0] = nodes[rank][1]

    return xs, table


def setup_hermite_table(nodes):
    """
    Return xs list and a divided differences jagged 2d list filled
    with initial values.
    """
    # setting up xs list and an empty table:
    xs = []
    node_num = len(nodes)
    for node in nodes:
        if len(node) == 3:
            node_num += len(node[2])
            xs += [node[0]]*(len(node[2]) + 1)
        else:
            xs.append(node[0])

    table = [[None for _ in range(node_num-i)] for i in range(node_num)]

    # filling the table with initial values:
    table_index = 0
    for node in nodes:
        if len(node) == 3:
            ders = node[2]

            for i in range(1 + len(ders)):
                table[table_index + i][0] = node[1]

                for j in range(len(ders) - i):
                    table[table_index + i][1 + j] = ders[j]/math.factorial(j+1)

            table_index += len(ders)
        else:
            table[table_index][0] = node[1]

        table_index += 1

    return xs, table


def divdiffs(nodes):
    """
    Return xs list and a jagged list of divided differences
    for a list of interpolations nodes, be it for Newton's or Hermite's
    interpolation.
    """
    hermite = False
    for node in nodes:
        if len(node) == 3:
            hermite = True
            break

    xs, table = (setup_hermite_table(nodes) if hermite
                 else setup_newton_table(nodes))

    for i in range(1, len(table)):
        for j in range(len(table[i])):
            if table[j][i] is None:
                table[j][i] = ((table[j][i - 1] - table[j + 1][i - 1]) /
                               (xs[j] - xs[i + j]))

    return xs, table
    